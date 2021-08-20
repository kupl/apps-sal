n = int(input())
xu = [list(input().split()) for i in range(n)]
ans = 0
for i in range(n):
    xu[i][0] = float(xu[i][0])
    if xu[i][1] == 'JPY':
        ans += xu[i][0]
    else:
        ans += xu[i][0] * 380000
print(ans)
