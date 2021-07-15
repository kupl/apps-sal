def main2():
    input()
    s = input()
    pair = [-1] * 2
    ans = s
    idx = 0
    for idx in range(0, len(s)):
        for i in range(idx, len(s)):
            if s[i] == '(':
                pair[0] = i if pair[0] == -1 else pair[0]
            elif s[i] == ')':
                pair[1] = i
                break
        if pair[0] != -1 and pair[1] != -1:
            s = s[:pair[0]] + ' ' + s[pair[0]+1:pair[1]] + ' ' + s[pair[1]+1:]
        elif pair[0] != -1 and pair[1] == -1:
            s = s[:pair[0]] + ' ' + s[pair[0]+1:]
            ans = ans + ')'
        elif pair[0] == -1 and pair[1] != -1:
            s = s[:pair[1]] + ' ' + s[pair[1]+1:]
            ans = '(' + ans
        pair = [-1] * 2
    print(ans)


def __starting_point():
    main2()
__starting_point()
