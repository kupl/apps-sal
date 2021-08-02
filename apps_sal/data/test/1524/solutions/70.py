S = input()
l = len(S)
A = [0] * l
c = 0
for i in range(l - 1):
    if S[i] == 'R':
        c += 1
    if S[i + 1] == 'L' or (i == l - 1 and S[-1] == 'R'):
        if i == l - 1 and S[-1] == 'R':
            c += 1
        A[i] += (c + 1) // 2
        A[i + 1] += c // 2
        c = 0
c = 0
for i in range(l - 1, 0, -1):
    if S[i] == 'L':
        c += 1
    if S[i - 1] == 'R' or (i == 0 and S[0] == 'L'):
        if i == 0 and S[0] == 'L':
            c += 1
        A[i] += (c + 1) // 2
        A[i - 1] += c // 2
        c = 0
print(' '.join(map(str, A)))
