from collections import deque
n,q = map(int,input().split())
z = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    z[a].append(b)
    z[b].append(a)
l = [list(map(int,input().split())) for i in range(q)]
p,x = [list(i) for i in zip(*l)]
c = [0] * n
for i in range(q):
    c[p[i]-1] += x[i]
queue = deque([1])
check = [1] * (n+1)
while queue:
    p = queue.popleft()
    if check[p]:
        for i in z[p]:
            if check[i]:
                c[i-1] += c[p-1]
                queue.append(i)
    check[p] = 0
print(' '.join(map(str,c)))
