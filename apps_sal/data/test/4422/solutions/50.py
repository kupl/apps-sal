N, K = map(int, input().split())
S = str(input())
A = ''
for i in range(N):
    if i + 1 == K:
        A += S[i].lower()
    else:
        A += S[i]
print(A)
