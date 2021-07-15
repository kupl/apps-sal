N = int(input())
liA = list(map(int, input().split()))
liB = list(map(int, input().split()))
liC = list(map(int, input().split()))

Manzoku = sum(liB)

for i in range(N):
    if i < N - 1:
        if liA[i+1] - liA[i] == 1:
            Manzoku += liC[liA[i] - 1]

print((Manzoku))
