import sys

n = int(sys.stdin.readline())

result = []
if(n % 2 == 0):
    for i in range(1, int(n / 2) + 1):
        t = i * 2
        result.append(str(t))
        result.append(str(t - 1))
    print(" ".join(result))
else:
    print(-1)
