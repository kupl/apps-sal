N, K = map(int, input().split())
# Nが十進数のとき、NよりKのi乗が超えた数のとき、
# iがK進数の桁数
for i in range(10 ** 9):
    if N < K ** i:
        print(i)
        break
