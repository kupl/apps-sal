def tennis(n):
    u, v = 1, 2
    j = 1
    while v <= n:
        u, v = v, u + v
        j += 1
    return j - 1


print(tennis(int(input())))
