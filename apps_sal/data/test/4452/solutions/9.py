for _ in range(int(input())):
    n = int(input())
    l = []
    i = 0
    while n:
        if n % 10:
            l.append(n % 10 * 10 ** i)
        i += 1
        n //= 10
    print(len(l))
    print(*l)
