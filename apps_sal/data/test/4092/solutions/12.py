import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

S = [0]
for a in A:
    S.append(S[-1] + a)

ANS = 0
SET = set()
for i in range(n + 1):
    if S[i] in SET:
        ANS += 1
        SET = {S[i], S[i - 1]}
    else:
        SET.add(S[i])

print(ANS)
