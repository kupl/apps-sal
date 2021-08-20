import math


def __starting_point():
    n = int(input())
    a = input().split()
    for i in range(n):
        a[i] = int(a[i])
    b = sum(a)
    a = list(set(a))
    n = len(a)
    improv = 0
    for i in range(n):
        for j in range(n):
            if a[i] < a[j]:
                found = False
                k = 2
                current = 0
                while not found:
                    if a[j] % k == 0:
                        found = True
                        current = max(a[i] + a[j] - a[i] * k - a[j] // k, current)
                    if found and k < math.sqrt(a[j] / a[i]):
                        found = False
                    k = k + 1
                improv = max(improv, current)
    print(b - improv)


__starting_point()
