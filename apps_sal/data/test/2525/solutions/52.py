from collections import deque
S = input()
Q = int(input())
cnt = 0
D = deque()
D.append(S)
for _ in range(Q):
    q = input()
    if q == '1':
        cnt += 1
    else:
        (q, f, c) = list(map(str, q.split()))
        f = int(f)
        if cnt % 2 == 0:
            if f == 2:
                D.append(c)
            else:
                D.appendleft(c)
        elif f == 2:
            D.appendleft(c)
        else:
            D.append(c)
X = ''.join(D)
print(X if cnt % 2 == 0 else X[::-1])
