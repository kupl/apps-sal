S = input()
N = len(S)
(a1, a2) = (0, 0)
for i in range(N):
    if i % 2 == 0 and S[i] == '1':
        a1 += 1
    if i % 2 == 1 and S[i] == '0':
        a1 += 1
for i in range(N):
    if i % 2 == 0 and S[i] == '0':
        a2 += 1
    if i % 2 == 1 and S[i] == '1':
        a2 += 1
print(min(a1, a2))
