for test_i in range(int(input())):
    s = input()
    print('DA' if min(s.count('0'), s.count('1')) % 2 else 'NET')
