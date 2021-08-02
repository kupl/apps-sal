n = int(input())
v = [int(x.strip()) for x in input().split()]
vs = sorted(v)
ans = 0
for i in range(n):
    a = (vs[i] / (2**(n - max(i, 1))))
    ans += a
print(ans)
