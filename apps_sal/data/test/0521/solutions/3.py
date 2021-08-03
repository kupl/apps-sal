while True:
    n = int(input())
    s = input()

    for i in range(0, n - 1):
        if s[i] == s[i + 1] and s[i] != '?':
            print('No')
            break

    else:
        if '??' in s or 'Y?Y' in s or 'C?C' in s or 'M?M' in s or s[0] == '?' or s[-1] == '?':
            print('Yes')
        else:
            print('No')

    break
