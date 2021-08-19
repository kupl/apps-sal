def readInts():
    return list(map(int, input().split()))


n = int(input())
a = int(input())
b = int(input())
c = int(input())
if a <= b - c or b > n:
    print(n // a)
else:
    tot = n - b
    cost = b - c
    ret = tot // cost + 1 + (tot % cost + c) // a
    print(ret)
