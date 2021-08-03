N = int(input())


def rec(n):
    if n % 2 == 0:
        return rec(n / 2) + 1
    else:
        return 0


m, c = 0, 1
for i in range(1, N + 1):
    if m < rec(i):
        m = rec(i)
        c = i
print(c)
