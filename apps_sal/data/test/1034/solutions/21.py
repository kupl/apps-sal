X, Y, Z, K = list(map(int, input().split()))
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
C = sorted(list(map(int, input().split())), reverse=True)
e = []
s = []

for i in A:
    for j in B:
        e.append(i+j)
e = sorted(e, reverse=True)

if K<len(e):
    e = e[0:K]

for i in e:
    for j in C:
        s.append(i+j)

s = sorted(s, reverse=True)

for i in range(K):
    print(s[i])
