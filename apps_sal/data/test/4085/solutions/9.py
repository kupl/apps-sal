for Valerchiclox in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    const = c[0] * c[-1]
    k = -1
    for i in c:
        if i * c[k] != const:
            const = -1
            break
        k -= 1
    if const == -1:
        print(const)
    else:
        s = 0
        for i in range(2, int(const ** 0.5) + 1):
            if const % i == 0:
                s += 1
        if s * 2 - n % 2 == n:
            print(const)
        else:
            print(-1)
