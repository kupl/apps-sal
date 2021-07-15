N = int(input())
A = list(map(int, input().split()))
table = []

for i, a in enumerate(A):
    table.append([a,i])
table.sort()

# DP[i][j] 左端に i 個, 右端に j 個貪欲に詰めたときのうれしさ
DP = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(1,N+1):
    # i 人目 table[i-1] の幼児を移動させる
    baby, pos = table.pop()
    
    DP[i][0] = DP[i-1][0] + baby * abs(pos-i+1)
    DP[0][i] = DP[0][i-1] + baby * abs(pos-(N-i))
    for x in range(1,i):
        y = i - x

        #左端に置く場合と右端に置く場合でmax
        DP[x][y] = max(DP[x-1][y] + baby * abs(pos-x+1),\
                     DP[x][y-1] + baby * abs(pos-(N-y)))

ans = 0
for i in range(N+1):
    ans = max(ans, DP[i][N-i])
print(ans)

