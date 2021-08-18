def main():
    input()
    s = input()
    zeros = s.count('0')
    print('1' + '0' * zeros if s != '0' else '0')


main()
