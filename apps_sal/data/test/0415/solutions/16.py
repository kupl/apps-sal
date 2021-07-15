from itertools import accumulate


def check(p):
    if p == 0:
        return True

    for i in range(n - p + 1):
        if acc[i + p] - acc[i] > 100 * p:
            return True

    return False


n = int(input())
r = list(map(int, input().split()))

acc = [0] + list(accumulate(r))

for k in range(n, -1, -1):
    if check(k):
        print(k)
        break

