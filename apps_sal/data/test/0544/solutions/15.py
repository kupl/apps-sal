for _ in range(int(input())):
    n = int(input())
    s = input()
    s2 = s[::-1]
    fail = False
    for i in range(len(s)):
        diff = abs(ord(s[i]) - ord(s2[i]))
        if diff and diff != 2:
            print('NO')
            fail = True
            break
    if not fail:
        print('YES')
