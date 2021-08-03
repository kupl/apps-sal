import sys
if False:
    inp = open('A.txt', 'r')
else:
    inp = sys.stdin

n = int(inp.readline())
ans = 0
if n % 2 != 0:
    print(0)
else:
    if n % 4 == 0:
        print(n // 4 - 1)
    else:
        print(n // 4)
