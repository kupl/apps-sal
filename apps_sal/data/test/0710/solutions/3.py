n = int(input())
s = input()
A,C,T,G = [], [], [], []

def dis(n, c):
    return min((ord(n) - ord(c)) % 26, (ord(c) - ord(n)) % 26)

for c in s:
    A.append(dis(c, 'A'))
    C.append(dis(c, 'C'))
    T.append(dis(c, 'T'))
    G.append(dis(c, 'G'))

res = 10 ** 1000
for i in range(n - 3):
    res = min(res, A[i] + C[i + 1] + T[i + 2] + G[i + 3])
print(res)

