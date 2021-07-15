n = int(input())
sss = list(map(int, input().split()))

ans = 0
for c in range(1, n // 2):
    a = n - 1 - c
    k = c
    tmp = 0
    while a > c and a != k and a + c != k:
        tmp += sss[a] + sss[k]
        ans = max(ans, tmp)
        a -= c
        k += c
print(ans)

