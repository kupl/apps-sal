n = int(input())
ans = 0
for j in range(1, n + 1):
    a = j
    d = n // j
    tmp = (a + a * d) * d // 2
    ans += tmp
print(ans)
