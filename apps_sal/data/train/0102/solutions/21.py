t = int(input())
for _ in range(t):
    n = input()
    l = len(n)
    n = int(n)
    c = 0
    for i in range(1, 10):
        x = i
        while x <= n:
            c += 1
            x = int(str(x) + str(i))
    print(c)

