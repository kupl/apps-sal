S = input()
N = len(S)
a = 1
z = 1
for i in range(N):
    if S[i] == 'A':
        break
    else:
        a += 1
for j in range(1, N + 1):
    if S[-j] == 'Z':
        break
    else:
        z += 1
ans = N - a - z + 2
print(ans)
