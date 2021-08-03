def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    if len(a) <= 2:
        print(0)
        return

    final_ans = n + 1
    for start, change_start in [(a[0], False), (a[0] - 1, True), (a[0] + 1, True)]:
        for end, change_end in [(a[-1], False), (a[-1] - 1, True), (a[-1] + 1, True)]:
            d, r = divmod(end - start, n - 1)
            if r == 0:
                b = start
                ans = 0
                if change_start:
                    ans += 1
                if change_end:
                    ans += 1

                impossible = False
                for i in range(1, n - 1):
                    if impossible:
                        break
                    if a[i] - b == d:
                        b += d
                    elif a[i] - b == d + 1 or a[i] - b == d - 1:
                        ans += 1
                        b += d
                    else:
                        impossible = True

                if not impossible:
                    final_ans = min(final_ans, ans)

    if final_ans < n + 1:
        print(final_ans)
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
