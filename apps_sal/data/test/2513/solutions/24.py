N = int(input())
S = input()
a = ['SS', 'SW', 'WS', 'WW']
for i in range(N):
    for j in range(4):
        a[j] += 'SW'[::-1 if S[i] == 'o' else 1][a[j][i] == a[j][i + 1]]
for i in range(4):
    if a[i][1] == a[i][N + 1] and a[i][0] == a[i][N]:
        print(a[i][1:N + 1])
        break
else:
    print(-1)
