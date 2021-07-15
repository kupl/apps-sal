N = int(input())
L = []
for i in range(N):
    t = list(map(int, input().split()))
    L.append(t)

L.insert(0, [0,0,0])

for i in range(1, N+1):
    time = abs(L[i-1][0] - L[i][0])
    distance = abs(L[i-1][1] - L[i][1]) + abs(L[i-1][2] - L[i][2])
    if (time < distance) or (time%2 != distance%2):
        print('No')
        return

print('Yes')

