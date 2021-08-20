n = int(input())
a = list(map(int, input().split()))
snuke = sum(a)
arai = 0
ans = 10 ** 20
for i in range(n - 1):
    snuke -= a[i]
    arai += a[i]
    ans = min(ans, abs(snuke - arai))
print(ans)
