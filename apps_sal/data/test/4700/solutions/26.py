n, m = map(int,input().split())
H = list(map(int,input().split()))
AB = []
ans = 0
for i in range(m):
    AB.append(list(map(int,input().split())))
    AB[-1][0] -= 1
    AB[-1][1] -= 1
ok = [1]*n
for i in range(m):
    if H[AB[i][0]] >= H[AB[i][1]]:
        ok[AB[i][1]] = 0
    if H[AB[i][0]] <= H[AB[i][1]]:
        ok[AB[i][0]] = 0
for i in ok:
    if i:
        ans += 1
print(ans)
