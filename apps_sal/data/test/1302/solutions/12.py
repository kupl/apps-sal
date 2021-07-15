3

def readln(): return tuple(map(int, input().split()))

n, k = readln()
if n == k:
    print(-1)
else:
    print(*(list(range(2, n - k + 1)) + [1] + list(range(n - k + 1, n + 1))))

