def main():
    n, k = [int(x) for x in input().split()]
    s = input()
    s = ''.join(sorted(s))

    count = 0
    last = None
    ans = 0

    for i, c in enumerate(s):
        if i == 0:
            last = c
            count += 1
            ans += ord(c) - 96

            if count == k:
                break

            continue

        if ord(c) - ord(last) < 2:
            continue

        last = c
        count += 1
        ans += ord(c) - 96

        if count == k:
            break

    else:
        print(-1)
        return

    print(ans)


def __starting_point():
    main()

__starting_point()
