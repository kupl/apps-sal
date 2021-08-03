N = int(input())
v = [int(x) for x in input().split()]
v.sort()
ans = (v[0] + v[1]) / 2.0
for i in range(2, N):
    ans = float(ans + v[i]) / 2
print(ans)
