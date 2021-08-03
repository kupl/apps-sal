t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(j) for j in input().split()]

    o = arr.count(1)
    z = arr.count(0)

    if o > z:
        if (n - z) % 2 == 1:
            print(n - z - 1)
            print(*([1] * (n - z - 1)))
        else:
            print(n - z)
            print(*([1] * (n - z)))
    else:
        print(n - o)
        print(*([0] * (n - o)))
