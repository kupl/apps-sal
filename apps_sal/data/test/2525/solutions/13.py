S = input()
Q = int(input())

flg = True
T, U = "", ""
for i in range(Q):
    q = list(input().split())
    if len(q) == 1:
        flg = not flg
    else:
        if flg:
            if q[1] == "1":
                T = q[2] + T
            else:
                U = U + q[2]
        else:
            if q[1] == "1":
                U = U + q[2]
            else:
                T = q[2] + T

S = T + S + U
if not flg:
    S = S[::-1]

print(S)
