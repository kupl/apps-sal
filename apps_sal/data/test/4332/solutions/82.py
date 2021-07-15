import sys
input = sys.stdin.readline

n = int(input())
s = 0
for i in range(len(str(n))):
    s += int(str(n)[i])
if n % s == 0:
    print('Yes')
else:
    print('No')
