n = int(input())
I = list(map(int, input().split()))
P = sorted(I)

sI = [0] * (n + 1)
sP = [0] * (n + 1)

for i in range(1, n + 1):
    sI[i] = sI[i - 1] + I[i - 1]
    sP[i] = sP[i - 1] + P[i - 1]

m = int(input())

for i in range(m):
    t, l, r = list(map(int, input().split()))
    if t == 1:
        print(sI[r] - sI[l - 1])
    else:
        print(sP[r] - sP[l - 1])
