# 入力
N, M = map(int, input().split())

# 番号を入力
A = [int(i) for i in range(N)]

B = []  # 台No. リスト

if N % 2 == 0:
    # N が偶数の場合

    center = N // 2
    c1 = center // 2
    c2 = center + c1
    # print(c1,c2)

    for i in range(1, M + 1):
        # print(i)
        j = i // 2
        # print("j", j)
        if i % 2 == 1:
            B.append((c1 - j, c1 + j + 1))
        else:
            B.append((c2 - (j - 1), c2 - (j - 1) + 2 * j))

else:
    # N が奇数の場合

    center = N // 2 + 1
    # print(center)
    for i in range(1, M + 1):
        B.append((center - i, center + i))

for i in B:
    print(i[0], i[1])
