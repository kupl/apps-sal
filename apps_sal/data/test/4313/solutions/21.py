n = int(input())
ans = 0
v = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
for i in range(n):
    if v[i] > c[i]:
        ans += v[i] - c[i]
print(ans)
