3


def readln():
    return tuple(map(int, input().split()))


(n,) = readln()
if n % 2:
    print(-1)
else:
    for i in range(0, n, 2):
        print(i + 2, i + 1, end=' ')
    print()
