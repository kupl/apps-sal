N = int(input())
S = input()
c = S.count
x = c('R') * c('G') * c('B')
c = 0
for i in range(N):
    for j in range(i + 1, N):
        if S[i] != S[j]:
            k = 2 * j - i
            if k < N and S[k] != S[i] and (S[k] != S[j]):
                x -= 1
print(x)
