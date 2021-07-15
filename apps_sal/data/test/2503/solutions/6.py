# D - Checker

N, K = map(int, input().split())
g = [[0]*K for _ in range(K)] # PDF解説通り2K*2K範囲でやると市松模様の処理が大変なのでK*Kの範囲で計算

for _ in range(N):
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    tmp = (x//K + y//K) % 2
    x %= K
    y %= K
    if (tmp == 0 and c == "B") or (tmp == 1 and c == "W"):
        g[x][y] += 1
    else:
        g[x][y] -= 1 # 白希望の点を-1で記録する

for i in range(K):
    for j in range(1,K):
        g[i][j] += g[i][j-1]

for i in range(1,K):
    for j in range(K):
        g[i][j] += g[i-1][j]

# [i,j]を黒範囲の左下の点とする。[0,i] * [0,j] の範囲または[i+1,K-1] * [j+1,K-1]の範囲にある黒希望点の個数を足し、白希望の点の個数を引く
# 上記範囲外にある白希望の点の個数を足し、黒希望の点の個数を引く
ans = 0
for i in range(K):
    for j in range(K):
        n_satisfied = g[-1][-1] -2*(g[-1][j] + g[i][-1]) + 4*g[i][j]
        ans = max(ans, (N + n_satisfied)//2, (N - n_satisfied)//2) # ((希望通りの点 + 希望通りでない点) + (希望通りの点 - 希望通りでない点))//2

print(ans)
