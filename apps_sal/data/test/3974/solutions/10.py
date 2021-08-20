def main():
    s = input()
    cnt = 0
    ans = 0
    for x in s:
        if x == '+':
            cnt += 1
            ans = max(ans, cnt)
        elif cnt == 0:
            ans += 1
        else:
            cnt -= 1
    print(ans)


def __starting_point():
    main()


__starting_point()
