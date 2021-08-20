3


def readln():
    return tuple(map(int, input().split()))


(n, k) = readln()
for i in range(n):
    print(*[k if i == j else 0 for j in range(n)])
