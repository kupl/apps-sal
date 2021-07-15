N = int(input())
T = [int(a) * 2 for a in input().split()]
V = [int(a) * 2 for a in input().split()]
MA = [0] * (sum(T) + 1)
a = 0
for i in range(N):
    for j in range(T[i]):
        a += 1
        MA[a] = min(MA[a-1] + 1, V[i])
MA[a] = 0
for i in range(N)[::-1]:
    for j in range(T[i]):
        a -= 1
        MA[a] = min(MA[a], MA[a+1] + 1, V[i])

print(((sum(MA[1:]) + sum(MA[:-1])) / 8))

