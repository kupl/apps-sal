# N問の問題が用意されている
N = int(input())
# 問題を解くのにかかる時間
T = list(map(int, input().split()))

# ドリンクの種類M
M = int(input())
# ドリンクを飲んだ場合の時間をリストに格納する
X = []

# まずはドリンクを飲んだ場合の時間をXに格納する
for i in range(M):
    X.append(list(map(int,input().split())))
    X[i][0] = X[i][0]-1

Y = []
# それぞれの問題の解く時間を取得する
for i in range(N):
    Y.append(T[i])
    
for i in range(len(X)):
    Y_copy = Y.copy()
    Y_copy[X[i][0]] = X[i][1]
    print(sum(Y_copy))
