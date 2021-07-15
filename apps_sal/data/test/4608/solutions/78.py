def f():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    x = 1
    c = 0
    for i in range(n):
        if x != 2:
            x = a[x-1]
            c += 1
            if c == n:
                return -1
        else:
            return c
print(f())
