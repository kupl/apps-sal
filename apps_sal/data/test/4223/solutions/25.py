N = int(input())
S = input()

ANS = 0
for i in range(N - 1):
    if S[i] != S[i + 1]:
        ANS += 1

print(ANS + 1)
