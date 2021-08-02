from collections import deque
q = deque(); K = int(input()); a = q.append; a((1, 1)); m = {}
while len(q):
    n, s = q.popleft()
    if not n in m: m[n] = s; q.appendleft((n * 10 % K, s)); a(((n + 1) % K, s + 1))
print(m[0])
