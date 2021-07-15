n, m = list(map(int, input().split()))
won = [0] * n
vot = [list(map(int, input().split())) for i in range(m)]
for i in range(m):
    ma = max(vot[i])
    for j in range(n):
        if vot[i][j] == ma:
            won[j] += 1
            break
ma = max(won)
for i in range(n):
    if ma == won[i]:
        print(i + 1)
        return
        

