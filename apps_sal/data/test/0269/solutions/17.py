

s = input()

M_inv = {}

A = [0] * 4

for i in range(len(s)):
    if s[i] != '!':
        M_inv[s[i]] = i % 4

for i in range(len(s)):
    if s[i] == '!':
        A[i % 4] += 1

print((str(A[M_inv['R']]) + " " + str(A[M_inv['B']]) + " " +
      str(A[M_inv['Y']]) + " " + str(A[M_inv['G']])))


