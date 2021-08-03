n = int(input())
ans = 10000000000
a = [int(i) for i in input().split()]
for i in range(0, n):
    d = 0
    for j in range(n):
        d += 2 * a[j] * (abs(i - j) + j + i)
    ans = min(ans, d)
print(ans)
