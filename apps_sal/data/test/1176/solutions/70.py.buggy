n = int(input())
lis = list(map(int, input().split()))

if 0 in lis:
    ans = 0
    for i in lis:
        if i < 0:
            ans += -1 * i
        else:
            ans += i
    print(ans)
    return

minus = [0] * n
for i in range(n):
    if lis[i] < 0:
        minus[i] = 1

if sum(minus) % 2 == 0:
    ans = 0
    for i in lis:
        if i < 0:
            ans += -1 * i
        else:
            ans += i
    print(ans)
else:
    ans = 0
    m = 10**9 + 1
    for i in lis:
        if i < 0:
            ans += -1 * i
        else:
            ans += i
        m = min(m, abs(i))
    print((ans - 2 * m))
