for _ in range(int(input())):
    n = int(input())
    p = [0] + list(map(int, input().split()))
    array = []
    for i in range(1, n + 1):
        c = 1
        k = p[i]
        while k != i:
            k = p[k]
            c += 1
        array.append(c)
    print (*array)
