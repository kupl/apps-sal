n, x = list(map(int, input().split()))
ans = n
mi = 10**4
for i in range(n):
    m = int(input())
    x -= m
    mi = min(m, mi)
ans += (x // mi)
print(ans)
