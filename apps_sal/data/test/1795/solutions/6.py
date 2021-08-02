def run():
    input()
    s = [int(x) for x in input().split()]

    for i in range(len(s)):
        s1 = s[i]
        s2 = s[s1 - 1]
        s3 = s[s2 - 1]
        if s3 - 1 == i:
            print('YES')
            return
    print('NO')


run()
