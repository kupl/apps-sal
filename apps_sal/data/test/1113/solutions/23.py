def main():
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    s = set([-1])
    for i in range(n):
        if arr[i] - 1 not in s:
            print(i + 1)
            return
        s.add(arr[i])
    print(-1)


def __starting_point():
    main()


__starting_point()
