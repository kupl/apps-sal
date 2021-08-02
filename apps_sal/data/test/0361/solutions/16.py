def main(s):
    key = "CODEFORCES"
    for i in range(11):
        s1 = key[0:i]
        s2 = key[i:10]
        if s.startswith(s1) and s.endswith(s2):
            return 'YES'
    return 'NO'


def __starting_point():
    s = input()
    print(main(s))


__starting_point()
