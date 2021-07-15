n = int(input())
a = list(map(int, input().split()))
a1 = sorted([a[i] * (n - i) * (i + 1) for i in range(n)])
b = sorted(list(map(int, input().split())), key=lambda x: -x)
ans = 0
c = 998244353
for i in range(n):
    ans = (ans + a1[i] * b[i]) % c
print(ans)

