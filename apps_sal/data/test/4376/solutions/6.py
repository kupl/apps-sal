T = input().split(' ')
n = int(T[0])
m = int(T[1])
P = input().split(' ')
for i in range(len(P)):
    P[i] = int(P[i])
for i in range(1, len(P)):
    P[i] += P[i - 1]
Q = input().split(' ')
for i in range(len(Q)):
    Q[i] = int(Q[i])
a = 0
b = 0
c = 0
d = 0
while c < len(Q):
    b = Q[c]
    if b > P[a]:
        d = P[a]
        a += 1
    else:
        print(a + 1, end=' ')
        print(b - d)
        c += 1
