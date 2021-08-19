N = int(input())
S = str(input())
(l, r) = (0, 0)
(p, m) = (0, 0)
for i in range(N):
    if S[i] == '(':
        l += 1
    else:
        r += 1
    if l < r:
        p += 1
        l += 1
m = l - r
for i in range(p):
    print('(', end='')
print(S, end='')
for i in range(m):
    print(')', end='')
