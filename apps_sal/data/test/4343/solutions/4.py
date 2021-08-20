N = int(input())
s = input()
t = input()


def stoi(s):
    return ord(s) - 97


def itos(i):
    return chr(97 + i)


def stoL(s):
    L = []
    for ss in s:
        L.append(stoi(ss))
    return L


A = stoL(s)
B = stoL(t)
C = [A[i] + B[i] for i in range(N)]
for i in range(1, N)[::-1]:
    if C[i] >= 26:
        C[i] -= 26
        C[i - 1] += 1
t = 0
for i in range(N):
    if C[i] % 2:
        C[i] = (C[i] + t - 1) // 2
        t = 26
    else:
        C[i] = (C[i] + t) // 2
        t = 0
u = ''
for c in C:
    u += itos(c)
print(u)
