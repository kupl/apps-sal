for _ in range(int(input())):
    n = int(input())
    s = input()
    if s == '0' * n or s == '1' * n:
        print(s)

    else:

        i = 0
        while s[i] == '0':
            i += 1
        j = n - 1
        while s[j] == '1':
            j -= 1
        if '1' in s[i:j + 1] and '0' in s[i:j + 1]:
            print(s[:i] + '0' + s[j + 1:])
        else:
            print(s)
