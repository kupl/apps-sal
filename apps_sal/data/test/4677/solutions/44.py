from sys import stdin
input = stdin.readline

S = input().strip()
P = ''
for s in S:
    if s == 'B':
        if P != '':
            P = P[:-1]
    else:
        P = P + s
print(P)
