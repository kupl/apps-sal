def main():
    s = input()
    t = input()
    ans = 'No'
    s2 = s * 2
    for i in range(len(s2)):
        if t == s2[i:i + len(s)]:
            ans = 'Yes'
            break
    print(ans)


def __starting_point():
    main()


__starting_point()
