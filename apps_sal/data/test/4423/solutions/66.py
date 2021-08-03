N = int(input())
shop = []
for i in range(N):
    S, P = input().split()
    P = int(P)
    shop.append([S, 100 - P, i])
shop.sort()
for i in range(N):
    print((shop[i][2] + 1))
