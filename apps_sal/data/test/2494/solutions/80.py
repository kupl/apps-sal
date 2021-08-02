from collections import*
q = deque([(1, 1)])
k = int(input())
m = {}
while q:
    n, s = q.pop()
    if(n in m) - 1: m[n] = s; q += (n * 10 % k, s), ; q.appendleft((-~n % k, s + 1))
print(m[0])
