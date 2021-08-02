N = int(input())
V = list(map(int, input().split()))
if N == 2:
    print((V[0] + V[1]) / 2)
else:
    V.sort()
    kati = V[0]
    for i in range(1, N):
        kati = (kati + V[i]) / 2
    print(kati)
