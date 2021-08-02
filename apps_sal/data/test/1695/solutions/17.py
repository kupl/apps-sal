from collections import Counter
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))


LIST = [[] for i in range(m)]

for i in range(n):
    s = input()
    for j in range(m):
        LIST[j].append(s[j])

SCORE = list(map(int, input().split()))
ANS = 0

for i in range(m):
    ANS += max(Counter(LIST[i]).values()) * SCORE[i]

print(ANS)
