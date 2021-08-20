S = input()
c = 0
N = len(S)
for i in range(N // 2):
    c += S[i] != S[N - i - 1]
print(c)
