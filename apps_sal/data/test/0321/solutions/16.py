from math import sqrt, floor


def check(n):
    for i in range(2, floor(sqrt(n)) + 1):
        if (n % i == 0):
            return False

    return True


t = int(input())

for i in range(t):
    a, b = list(map(int, input().split()))

    if (a - b == 1 and check(a + b)):
        print("YES")
    else:
        print("NO")
