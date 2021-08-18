N, K = map(int, input().split())
L = []
mini = float('inf')

for i in range(N):
    h = int(input())
    L.append(h)

L.sort(reverse=True)

for i in range(len(L) - K + 1):
    if L[i] - L[i + K - 1] < mini:
        if L[i] - L[i + K - 1] == 0:
            print(0)
            return
        else:
            mini = L[i] - L[i + K - 1]

print(mini)
