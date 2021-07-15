from collections import deque
n, m = tuple(map(int,input().split()))
li,s = deque([0]),set()

for i in range(m):
    a,b = map(int, input().split())
    a -= 1;b-=1
    s.add((a,b))
    s.add((b,a))
reach = (0, n-1) in s
d = [0]
d.extend([-1 for _ in range(n-1)])
while li:
    a =li.popleft()
    for b in range(n):
        if (not(reach and ((a, b) in s)))\
                and(reach or ((a, b) in s))\
                and (d[b] == -1 or d[b] > d[a] + 1):
            d[b] = d[a] + 1
            li.append(b)
print(d[n-1])
