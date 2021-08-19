

n, r = list(map(int, input().split()))
a = list(map(int, input().split()))
r -= 1


def f():
    prev = [0] * n
    last = -1
    for i in range(n):
        if a[i]:
            last = i
        prev[i] = last

    nb = 0
    i = 0
    while i < n:
        # find the rightmost heater covering i
        j = prev[min(i + r, n - 1)]
        if j < 0 or j + r < i:
            return -1
        nb += 1
        # next place to heat is the first not covered by the selected heater
        i = j + r + 1

    return nb


print(f())
