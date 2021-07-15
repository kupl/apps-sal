N, M = list(map(int, input().split()))
C = [tuple(map(int, input().split())) for _ in range(N)]

res = 0

for i in range(8):
    #絶対値を足す、引くの2パターンで表現する
    
    #ケーキの値の合計を入れる配列
    D = [0 for _ in range(N)]

    #対応するbitが1なら足す、0なら引く
    for j in range(N):
        x, y, z = C[j]
        if (i >> 0) & 1:
            D[j] += x
        else:
            D[j] -= x
        if (i >> 1) & 1:
            D[j] += y
        else:
            D[j] -= y
        if (i >> 2) & 1:
            D[j] += z
        else:
            D[j] -= z

    #価値が高い順にM個選ぶ
    D.sort(reverse=True)
    res = max(res, sum(D[:M]))

print(res)

