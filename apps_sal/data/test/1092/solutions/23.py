import math


def solve(n, list1):
    list1.sort()
    inf = int(1000000000.0 + 7)
    t1 = [list1[0] - 1, n - list1[-1]]
    t2 = []
    for i in range(1, len(list1)):
        t2.append(list1[i] - list1[i - 1] - 1)
    num1 = 1
    for i in range(n - len(list1)):
        num1 = num1 * (i + 1)
        num1 = num1 % inf
    num2 = 1
    num2 = math.factorial(t1[0]) % inf
    num2 = num2 % inf
    num2 = num2 * math.factorial(t1[1]) % inf
    num2 = num2 % inf
    for i in range(len(t2)):
        num2 = num2 * math.factorial(t2[i])
        num2 = num2 % inf
    num2 = pow(num2, inf - 2, inf)
    num3 = 1
    for i in range(len(t2)):
        if t2[i] - 1 < 0:
            continue
        num3 = num3 * pow(2, t2[i] - 1, inf) % inf
    num1 = num1 * num2
    num1 = num1 % inf
    num1 = num1 * num3
    num1 = num1 % inf
    return int(num1)


(n, m) = map(int, input().split())
list1 = list(map(int, input().split()))
print(solve(n, list1))
