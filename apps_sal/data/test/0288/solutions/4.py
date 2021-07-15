def solve(n):
    k = 0
    f1, f2 = 1, 2
    while not f1 <= n < f2:
        k += 1
        t = f1
        f1 = f2
        f2 = f1 + t
    return k

n = int(input())
print(solve(n))

