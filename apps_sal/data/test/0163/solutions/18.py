def main():
    n, k = list(map(int, input().split()))
    s = input()
    g, t = s.find('G'), s.find('T')
    if g < t:
        s = s[g:t + 1:k]
    else:
        s = s[t:g + 1:k][::-1]
    print(("NO", "YES")[s[0] == 'G' and s[-1] == 'T' and '


def __starting_point():
    main()


__starting_point()
