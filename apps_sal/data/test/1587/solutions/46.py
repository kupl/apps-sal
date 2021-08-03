import sys

N = int(input())
S = list(input())

c = min(S.count('R'), S.count('W'))
r = 0
count = 0
for l in range(N - c):
    if S[l] == 'W':
        for i in range(r, len(S) - c):
            if S[-(i + 1)] == 'R':
                S[-(i + 1)] = 'W'
                S[l] = 'R'
                count += 1
                break
            r = i

print(count)
