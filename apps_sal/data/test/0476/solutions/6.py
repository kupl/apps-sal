def main():
    s = str(input())
    ss = set(s)
    if s == '1':
        print('YES')
        return
    if s == '14':
        print('YES')
        return
    if s == '144':
        print('YES')
        return
    if s.find('444') != -1:
        print('NO')
        return
    f1 = s.find('1') != -1 or s.find('14') != -1 or s.find('14') != -1
    f2 = ss == {'1', '4'} or ss == {'1'}
    f3 = s.count('1') > 1
    f4 = s[0] == '1'
    if f1 and f2 and f3 and f4:
        print('YES')
    else:
        print('NO')


main()
