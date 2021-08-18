import math

n, a, b, k = list(map(int, input().split()))
h = list(map(int, input().split()))
ska = []
for i in range(0, n):
    totm = h[i] % (a + b)
    if totm == 0:
        totm = a + b
    ska.append(math.ceil(totm / a) - 1)
ska.sort()
cnt = 0
ans = 0
i = 0
while i < n and cnt + ska[i] <= k:
    ans += 1
    cnt += ska[i]
    i += 1
print(ans)
