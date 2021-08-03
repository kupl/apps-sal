n = int(input())
a = list(map(int, input().split()))
b = sorted(list(map(int, input().split())), reverse=True)

ans = 0

mmm = 998244353

c = sorted([a[i] * (i + 1) * (n - i) for i in range(n)])

for i in range(n):
    ans = (ans + c[i] * b[i]) % mmm

print(ans)
