(n, m) = list(map(int, input().split()))
a_lis = [list(map(int, input().split())) for i in range(n)]
c_lis = [list(map(int, input().split())) for i in range(m)]
for i in range(n):
    num = 0
    ans = 10 ** 10
    for j in reversed(list(range(m))):
        a = a_lis[i]
        c = c_lis[j]
        num = abs(a[0] - c[0]) + abs(a[1] - c[1])
        ans = min(ans, num)
        if num == ans:
            cnt = j + 1
    print(cnt)
