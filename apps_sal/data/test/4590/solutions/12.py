N, M, K = map(int, input().split())
lsA = list(map(int, input().split()))
lsB = list(map(int, input().split()))

lsAN = [0]
sumA = 0
for i in range(N):
    sumA += lsA[i]
    lsAN.append(sumA)
lsBN = [0]
sumB = 0
for i in range(M):
    sumB += lsB[i]
    lsBN.append(sumB)
j = M
ans = 0
for i in range(N + 1):
    if lsAN[i] > K:
        break
    while lsBN[j] > K - lsAN[i]:
        j -= 1
    ans = max(ans, i + j)
print(ans)
