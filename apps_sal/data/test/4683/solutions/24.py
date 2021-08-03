n = int(input())
a = list(map(int, input().split()))
s = sum(a)
ans = 0
sub = 0

for i in range(n):
    ans += a[i] * s

for j in range(n):
    sub += a[j]**2

print(((ans - sub) // 2) % (10**9 + 7))
