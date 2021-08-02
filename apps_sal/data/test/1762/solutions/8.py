import heapq
def f(): return list(map(int, input().split()))


n, k = f()
p = [0] * k
q = [0] * n
for i in range(n):
    s, m = f()
    q[i] = max(p[0], s) + m
    heapq.heapreplace(p, q[i])
print('\n'.join(map(str, q)))
