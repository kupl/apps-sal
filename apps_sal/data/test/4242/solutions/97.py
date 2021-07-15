A, B, K = map(int, input().split())

kouyakusuu = []

for i in range(1 , A + 1):
    if A % i == 0 and B % i == 0:
        kouyakusuu.append(i)

print(kouyakusuu[-K])
