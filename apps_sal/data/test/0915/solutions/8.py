import sys
input = sys.stdin.readline

k = int(input())
S = "codeforces"
ANS = [1] * 10
NOW = 1
ind = 0
while NOW < k:
    ANS[ind] += 1
    NOW = NOW * ANS[ind] // (ANS[ind] - 1)
    ind = (ind + 1) % 10

for i in range(10):
    print(S[i] * ANS[i], end="")
print()
