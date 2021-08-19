def places(num, v):
    if num >= v + n:
        return 0
    if num < v:
        return n
    return n - (num - v)


def check(num):
    for i in range(n - 1, -1, -1):
        count = max(0, places(b[i], num) - (n - 1 - i))
        if count == 0:
            return True
        if count % p == 0:
            return False
    return False


def check2(num):
    for i in range(n - 1, -1, -1):
        count = max(0, places(b[i], num) - (n - 1 - i))
        if count % p == 0:
            return True
    return False


(n, p) = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(a)
minn = b[0]
maxx = b[-1]
low = 0
high = maxx - 1
while low < high:
    mid = (low + high) // 2
    if check(mid):
        low = mid + 1
    else:
        high = mid - 1
if check(low):
    start = low + 1
else:
    start = low
low = start
high = maxx - 1
while low < high:
    mid = (low + high) // 2
    if not check2(mid):
        low = mid + 1
    else:
        high = mid - 1
if check2(low):
    end = low - 1
else:
    end = low
ans = []
for i in range(start, end + 1):
    ans.append(i)
print(len(ans))
print(*ans)
