import collections


def solve():
    (n, b, a) = list(map(int, input().split()))
    a_max = a
    S = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if S[i] == 1:
            if a < a_max and b > 0:
                b -= 1
                a += 1
            elif a > 0:
                a -= 1
            elif b > 0:
                b -= 1
            else:
                return i
        elif a > 0:
            a -= 1
        elif b > 0:
            b -= 1
        else:
            return i
    return n


print(solve())
