N = int(input())
a = list(map(int, input().split()))
ans = float('inf')
snuke = 0
arai = sum(a)
for i in range(N - 1):
    snuke += a[i]
    arai -= a[i]
    ans = min(abs(snuke - arai), ans)
print(ans)
