N, X = map(int, input().split())
L = list(map(int, input().split()))
kyori = 0

for i in range(N):
    kyori += L[i]
    if kyori > X:
        print(i + 1)
        return

print(N + 1)
