import math

n, a, b = tuple(map(int, input().split()))


def mr(k, n):
    a = [0]
    for i in range(n // k):
        a.extend([i] * k)
    return a


rounds = {r: mr(2**r, 258) for r in range(1, 10)}
# print(len(rounds[1]))


def sol(a, b):
    for i in range(1, 10):
        if rounds[i][a] == rounds[i][b]:
            return i
    return 0


a = sol(a, b)


print(a if a != int(math.log(n, 2)) else "Final!")
