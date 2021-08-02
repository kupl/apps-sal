import sys
input = sys.stdin.readline
s = str(input()).replace('\n', '')
t = str(input()).replace('\n', '')

ans = len(t)

for i in range(len(s) - len(t) + 1):
    diff = 0
    for j in range(len(t)):
        if t[j] != s[i + j]:
            diff += 1
    if ans > diff:
        ans = diff
print(ans)
