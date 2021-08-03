def solve():
    n = int(input())

    ar = list(map(int, input().split()))

    prev = 0

    for i in range(n):
        if ar[i] - prev > 15:
            print(prev + 15)
            return
        prev = ar[i]
    print(min(90, prev + 15))


solve()
