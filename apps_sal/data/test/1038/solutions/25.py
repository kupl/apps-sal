def r(n):
    t = n % 4
    if t == 0:
        return n
    if t == 1:
        return 1
    if t == 2:
        return n + 1
    if t == 3:
        return 0


a, b = map(int, input().split())
print(r(a - 1) ^ r(b))
