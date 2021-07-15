S = input()
Q = int(input())
T = 0
s = ""
for i in range(Q):
    q = list(input().split())
    if q[0] == "1":
        T = (T+1) % 2
    elif (T == 0 and q[1] == "1") or (T == 1 and q[1] == "2"):
        s += q[2]
    else:
        S += q[2]
if T == 0:
    S = s[::-1] + S
    print(S)
else:
    S = S[::-1] + s
    print(S)
