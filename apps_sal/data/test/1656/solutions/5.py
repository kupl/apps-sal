import sys

s = sys.stdin.readline().strip()
n = len(s)

w = 0
wo = 0
wow = 0

for i in range (1, n):
    if s[i] == "v" and s[i-1] == "v":
        w = w + 1
        wow = wow + wo
    if s[i] == "o":
        wo = wo + w

print(wow)
