for _ in range(int(input())):
    a, k = tuple(map(int, input().split()))

    for i in range(k - 1):
        nums = [i for i in str(a)]
        delta = int(min(nums)) * int(max(nums))

        if delta == 0:
            break
        a += delta

    print(a)
