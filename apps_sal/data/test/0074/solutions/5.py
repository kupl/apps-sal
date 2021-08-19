import math


def Prost(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        return True


n = int(input())
r = 0
if Prost(n):
    print(1)
    print(n)
else:
    for i in range(n - 1, n - 300, -1):
        if Prost(i):
            r = i
            break
    k = n - r
    if k == 2:
        print(2)
        print(r, k)
    else:
        for i in range(2, k):
            if Prost(i) and Prost(k - i):
                print(3)
                print(r, i, k - i)
                break
