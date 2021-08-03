from collections import deque
n, m, q = map(int, input().split())
A = []
B = []
C = []
D = []
for i in range(q):
    a, b, c, d = map(int, input().split())
    A.append(a - 1)
    B.append(b - 1)
    C.append(c)
    D.append(d)

que = deque([[1]])
M = 0

while que:

    lst = que.popleft()
    if len(lst) == n:
        s = 0
        for i in range(q):
            if lst[B[i]] - lst[A[i]] == C[i]:
                s += D[i]
        if M < s:
            M = s

    else:
        for j in range(lst[-1], m + 1):
            lst2 = lst + [j]
            que.append(lst2)

print(M)
