N = int(input())  # 問題の数
T = list(map(int, input().split()))  # 問題を解くのにかかる時間
M = int(input())  # ドリンクの種類の数
for i in range(1, M + 1):
    tmp = list(map(int, input().split()))
    tmp2 = T[tmp[0] - 1]
    T[tmp[0] - 1] = tmp[1]
    print(sum(T))
    T[tmp[0] - 1] = tmp2
