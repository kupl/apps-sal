import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

ANS = [0] * 21

for a in A:
    for i in range(21):
        if a & (1 << i) != 0:
            ANS[i] += 1

S = 0
for i in range(n):
    K = 0
    for j in range(21):
        if ANS[j] > 0:
            ANS[j] -= 1
            K += 1 << j

    S += K * K

print(S)
