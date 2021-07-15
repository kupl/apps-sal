n = int(input())
vn = sorted(list(map(int, input().split())))
ans = vn[0]
for i in range(1, n):
    ans = (ans + vn[i]) / 2
print(ans)

