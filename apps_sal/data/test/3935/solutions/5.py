import sys
input = sys.stdin.readline
n = int(input())
B = list(map(int, input().split()))
ANS = [0] * 65
BANS = [0] * n
for i in range(n):
    b = B[i]
    score = 0
    while b % 2 == 0:
        b //= 2
        score += 1
    ANS[score] += 1
    BANS[i] = score
k = max(ANS)
ind = ANS.index(k)
print(n - k)
T = [B[i] for i in range(n) if BANS[i] != ind]
print(*T)
