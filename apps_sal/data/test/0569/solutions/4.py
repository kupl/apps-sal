from sys import stdin
input = stdin.readline
n = int(input())
s = input().rstrip('\n')
m = set()
for i in s:
    m.add(i)
if len(s) > 26:
    print(-1)
else:
    print(len(s) - len(m))
