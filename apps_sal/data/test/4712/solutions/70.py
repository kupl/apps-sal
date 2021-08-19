def main():
    (h, w) = list(map(int, input().split()))
    a = []
    for i in range(h):
        a.append(input())
    cnt = len(a[0]) + 2
    print('#' * cnt)
    for _ in a:
        print(f'#{_}#')
    print('#' * cnt)


def __starting_point():
    main()


__starting_point()
