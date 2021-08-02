N = int(input())
P = list(map(int, input().split()))

count = 1
minP = P[0]
for i in range(1, N):
    if minP > P[i]:
        count += 1
    minP = min(minP, P[i])
print(count)
