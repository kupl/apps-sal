def main():
    s = input()

    if s.count('444') > 0:
        print('NO')
        return()
    s = s.replace('144', '')
    s = s.replace('14', '')
    s = s.replace('1', '')
    if len(s) == 0:
        print('YES')
    else:
        print('NO')


main()
