import sys

S = input()

count = 0
ans = 0
for i in range(len(S)):
    if S[i] == 'R':
        count += 1
    else:
        count = 0
    ans = max(ans, count)

print(ans)
