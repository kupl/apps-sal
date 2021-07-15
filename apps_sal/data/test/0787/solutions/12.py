def main():
    n = int(input())
    s = input()
    result = []
    substring = []
    d = set()

    for i in range(len(s)):
        if n > 0 and s[i] not in d:
            if len(substring) > 0 :
                result.append(''.join(substring))
                substring = []
            substring.append((s[i]))
            d.add(s[i])
            n -= 1
        else:
            substring.append((s[i]))

    if len(substring) > 0 :
        result.append(''.join(substring))
    if n > 0:
        print('NO')
        return
    else:
        print('YES')
        for s in result:
            print(s)






def __starting_point():
    main()
__starting_point()
