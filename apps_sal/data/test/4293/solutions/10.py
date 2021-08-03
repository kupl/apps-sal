P, Q, R = map(int, input().split())
if P < Q:
    P, Q = Q, P
if P < R:
    P, R = R, P
print(Q + R)
