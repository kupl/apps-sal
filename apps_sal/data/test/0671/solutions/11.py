import sys
n = int(input())
s = ''
i = 0
while len(s) < n:
    i += 1
    s += str(i)
print(s[n - 1])
