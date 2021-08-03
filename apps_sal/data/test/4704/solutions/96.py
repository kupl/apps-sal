n = int(input())
a = list(map(int, input().split()))

sa = [0 for i in range(n)]
sc = sum(a)
c = 0
for i in range(n):
    c += a[i]
    sa[i] = c
ans = 10**10

for i in range(1, n):
    x = sc - sa[i - 1]
    v = abs(x - sa[i - 1])
    ans = min(ans, v)
print(ans)
