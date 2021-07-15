import sys

input = sys.stdin.readline

n = int(input())

s = input().strip()

found = False
for i in range(len(s) - 1):
    if s[i] > s[i + 1]:
        s = s[0:i] + s[i+1:]
        found = True
        break

if found:
    print(s)
else:
    print(s[:-1])
