import sys

n = int(sys.stdin.readline())

if(n <= 2):
    print(-1)
    return

res = []
for i in range(n, 0, -1):
    res.append(str(i))

print(" ".join(res))
