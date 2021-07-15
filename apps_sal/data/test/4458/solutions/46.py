n = int(input())
P = list(map(int, input().split()))
minSoFar = 2 * 10**5 + 1
ans = 0
for i in range(n):
    if P[i] < minSoFar:
        ans += 1
    minSoFar = min(minSoFar, P[i])
print(ans)
