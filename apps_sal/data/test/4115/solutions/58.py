S = input()
n = len(S)
c = 0
for i in range(n // 2):
    if S[i] != S[n - i - 1]:
        c += 1
print(c)
