
import time

n = int(input())
x = [int(i) for i in input().split()]

q = int(input())


x = sorted(x)
buy = [0]
j = 0

for i in range(1, x[n - 1] + 1):
    s = 0
    while(j < n and x[j] == i):
        s += 1
        j += 1
    buy.append(buy[i - 1] + s)

ans = []
for i in range(q):
    m = int(input())
    if m < len(buy):
        ans.append(buy[m])
    else:
        ans.append(n)

start = time.time()

for i in range(q):
    print(ans[i])

finish = time.time()
