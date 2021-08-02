for _ in range(int(input())):
    s = input()
    if '1' not in s:
        print(0)
    else:
        print(s.rindex('1') - s.index('1') - s.count('1') + 1)
