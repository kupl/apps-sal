n = int(input())
v = list(map(int, input().split()))
v = sorted(v)
ans = v[0]
for i in range(1, n):
    ans = (ans + v[i]) / 2
print('{:.6f}'.format(ans))
