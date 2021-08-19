(a, b) = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]
s = []
for p in range(b):
    s += [[int(i) for i in input().split()]]
S = []
k = 0
for p in range(b - 1, -1, -1):
    if s[p][1] > k:
        S += [s[p]]
        k = s[p][1]
Q1 = sorted(q[:S[-1][1]])
(x, y) = (0, S[-1][1] - 1)
S = [[0, 0]] + S
l = 1
for j in range(S[-1][1] - 1, -1, -1):
    if x > y:
        break
    if j < S[-l][1]:
        k = S[-l][0]
        l += 1
    if k == 1:
        q[j] = Q1[y]
        y -= 1
    if k == 2:
        q[j] = Q1[x]
        x += 1
print(' '.join(list(map(str, q))))
