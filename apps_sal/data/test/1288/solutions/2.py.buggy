def check(num):
    count = 0
    flag = -1
    s = 0
    for i in range(n):
        if a[i] <= num:
            count += 1
            s += 1
        else:
            if flag == -1:
                flag = s % 2
                count += 1
                s += 1
            else:
                if (s + 1) % 2 != flag:
                    count += 1
                    s += 1
        if count == k:
            return True
    return False


n, k = map(int, input().split())
a = list(map(int, input().split()))
if n == k:
    m1 = 0
    m2 = 0
    for i in range(0, n, 2):
        m1 = max(m1, a[i])
    for i in range(1, n, 2):
        m2 = max(m2, a[i])
    print(min(m1, m2))
    return
s = set(a)
minn, maxx = min(a), max(a)
low = minn
high = maxx
while low < high:
    mid = (low + high) // 2
    if check(mid):
        high = mid - 1
    else:
        low = mid + 1
if check(low):
    print(low)
else:
    print(low + 1)
