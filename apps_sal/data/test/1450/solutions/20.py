def main():
    s = list(map(int, input()))
    (cnt0, cnt1) = (0, 0)
    ans = []
    for a in s:
        if a == 1:
            cnt1 += 1
        elif a == 2:
            ans.append(a)
        elif a == 0:
            if not ans:
                cnt0 += 1
            else:
                ans.append(a)
    s = '0' * cnt0 + '1' * cnt1 + ''.join(map(str, ans))
    print(s)


def __starting_point():
    main()


__starting_point()
