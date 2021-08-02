for _ in range(int(input())):
    s = ''.join(sorted(input()))
    if s[0] == s[-1]:
        print('-1')
    else:
        print(s)
