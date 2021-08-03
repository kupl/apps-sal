def check(num):
    add = 0
    sub = [0] * (2 * n)
    for i in range(n):
        add -= sub[i]
        if (a[i] + add) < num:
            d = num - a[i] - add
            sub[i + w] = d
            add = num - a[i]
    # print (num,sub)
    count = 0
    for i in sub:
        count += i
    if count <= m:
        return True
    return False


n, m, w = map(int, input().split())
a = list(map(int, input().split()))
low = 0
high = min(a) + m
while low < high:
    mid = (low + high) // 2
    if check(mid):
        low = mid + 1
    else:
        high = mid - 1
if check(low):
    print(low)
else:
    print(low - 1)
