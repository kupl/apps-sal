S = input()
N = len(S)
if N % 2 == 1:
    M = N - 1
else:
    M = N - 2
for i in range(M, 0, -2):
    if S[:i // 2] == S[i // 2:i]:
        break
print(i)
