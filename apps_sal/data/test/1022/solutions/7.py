def main():
    n = int(input())
    left = [int(x) for x in input().strip().split()]
    right = [int(x) for x in input().strip().split()]
    rank = [x + y for (x, y) in zip(left, right)]
    arr = [(n - r) for r in rank]

    for i in range(n):
        more = 0
        for j in range(i):
            if arr[j] > arr[i]:
                more += 1
        if more != left[i]:
            print('NO')
            return

    for i in range(n):
        more = 0
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                more += 1
        if more != right[i]:
            print('NO')
            return

    print('YES')
    for x in arr:
        print(x, end=' ')
    print()


def __starting_point():
    main()


__starting_point()
