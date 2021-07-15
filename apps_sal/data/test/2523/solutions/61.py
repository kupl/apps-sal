S = list(input())
C = len(S)
for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        c = max(i + 1, len(S) - i - 1)
        C = min(C, c)
print(C)
