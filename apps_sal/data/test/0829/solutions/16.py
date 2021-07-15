import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
s = input()
zero = 0
for i in s:
    if i=='0': zero+=1
one = n-zero
if one!=zero:
    print(1)
    print(s)
else:
    print(2)
    print(s[:-1], s[-1])

