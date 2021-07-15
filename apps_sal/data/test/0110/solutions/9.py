n = int(input())
ai = list(map(int,input().split()))
for i in range(n):
    if ai[i] >= 0:
        ai[i] = -ai[i]-1
maxi = 0
maxn = 0
for i in range(n):
    if maxn < abs(ai[i]):
        maxn = abs(ai[i])
        maxi = i
if n % 2 != 0:
    ai[maxi] = -ai[maxi] - 1

for i in range(n):
    print(ai[i], end=" ")

