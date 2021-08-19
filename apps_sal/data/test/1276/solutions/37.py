N = int(input())
S = input()
x = S.count('R') * S.count('G') * S.count('B')
c = 0
for i in range(N):
    for j in range(i + 1, N):
        if S[i] != S[j]:
            k = 2 * j - i
            if k < N and S[k] != S[i] and (S[k] != S[j]):
                c += 1
print(x - c)
