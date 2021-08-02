n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
a = sorted(a, key=lambda x: x[1])
bridge = a[0][1] - 1
ans = 1

for i in range(1, m):
    if a[i][0] > bridge:
        bridge = a[i][1] - 1
        ans += 1

print(ans)
