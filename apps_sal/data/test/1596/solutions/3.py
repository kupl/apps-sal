s = input()
n = len(s)
A = []
mod = 10 ** 9 + 7
L = [0, 1, 2]
for i in range(10 ** 5 + 3):
    L.append((L[-1] + L[-2]) % mod)
nn = 0
uu = 0
for i in range(n):
    if s[i] == 'n':
        if nn == 0:
            nn = 1
            A.append(1)
        else:
            A[-1] += 1
    else:
        nn = 0
    if s[i] == 'u':
        if uu == 0:
            uu = 1
            A.append(1)
        else:
            A[-1] += 1
    else:
        uu = 0
ans = 1
for i in range(len(A)):
    ans = ans * L[A[i]] % mod
if s.count('m') > 0 or s.count('w') > 0:
    ans = 0
print(ans)
