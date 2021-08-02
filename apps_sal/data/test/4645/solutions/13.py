t = int(input())

while t != 0:
    t -= 1
    n = int(input())
    if n == 2 or n == 3:
        print(-1)
    else:
        odd = [i for i in range(1, n + 1, 2)]
        eve = [i for i in range(2, n + 1, 2)]
        odd.reverse()
        eve[0], eve[1] = eve[1], eve[0]
        odd += eve
        print(*odd)
