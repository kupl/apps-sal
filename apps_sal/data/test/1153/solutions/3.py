n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
ans = 0
i = 0
j = 0
sumx = 0
sumy = 0
while i < n and j < m:
    if sumx <= sumy:
        sumx += x[i]
        i += 1
    if sumy < sumx:
        sumy += y[j]
        j += 1
    if sumx == sumy:
        ans += 1
        sumx = 0
        sumy = 0
if i < n or j < m:
    ans += 1
print(ans)

