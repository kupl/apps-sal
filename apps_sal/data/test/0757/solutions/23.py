from sys import stdin
aux = list(map(int, stdin.readline().split()))
n = aux[0]
m = aux[1]
k = aux[2]
arr = list(map(int, stdin.readline().split()))
arr.sort(reverse=True)
ans = 0

if(m <= k):
    m = 0
else:
    m -= k - 1
for x in arr:
    if(m <= 0):
        break
    ans += 1
    m -= x - 1
    if(m == 1):
        m = 0

if(m <= 0):
    print(ans)
else:
    print(-1)
