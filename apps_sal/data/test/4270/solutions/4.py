N = int(input())
V = list(map(int, input().split()))
V.sort()

for i in range(N-1):
    V[i + 1] = (V[i] + V[i + 1])/2

print((V[N-1]))

