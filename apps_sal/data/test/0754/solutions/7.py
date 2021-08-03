import sys
inp = sys.stdin
n = int(inp.readline())
s = inp.readline()
cnt = 1
for i in range(1, n):
    if s[i] != s[i - 1]:
        cnt += 1
print(n - cnt)
