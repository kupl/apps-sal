from queue import Queue
import heapq

n, m = input().split()
n = int(n)
m = int(m)

f = [0] * (n + 1)
sol = [0] * (n + 1)
adya = [[] for _ in range(n + 1)]

for i in range(m):
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    adya[n2].append(n1)
    f[n1] += 1

cola = []
cnt = 0

for i in range(1, n + 1):
    if(f[i] == 0):
        heapq.heappush(cola, -1 * i)
        cnt += 1
num = int(n)
while(cnt > 0):
    v = heapq.heappop(cola)
    v *= -1
    sol[v] = num
    cnt -= 1
    num -= 1
    for to in adya[v]:
        f[to] -= 1
        if(f[to] == 0):
            heapq.heappush(cola, -1 * to)
            cnt += 1

stringOut = ""
for i in range(1, n + 1):
    stringOut += str(sol[i])
    if(i != n):
        stringOut += ' '

print(stringOut)
