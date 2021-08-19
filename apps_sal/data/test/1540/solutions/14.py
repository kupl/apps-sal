"""
YL 2 B. K6nelogi
"""
(n, m, k) = list(map(int, input().split()))
too = dict()
chat = dict()
chat2 = dict()
for i in range(n):
    too[i] = 0
for i in range(m):
    chat2[i] = 0
for i in range(n):
    chat[i] = list(map(int, input().split()))
for i in range(k):
    (x, y) = list(map(int, input().split()))
    chat2[y - 1] += 1
    too[x - 1] -= 1
out = []
for i in range(n):
    t2 = 0
    for e in range(m):
        if chat[i][e]:
            t2 += chat2[e]
    t = too[i] + t2
    out.append(str(t))
print(' '.join(out))
