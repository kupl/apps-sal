N = int(input())
S = input()
for i in range(1, N):
    if S[i - 1] == S[i]:
        N = N - 1
print(N)
