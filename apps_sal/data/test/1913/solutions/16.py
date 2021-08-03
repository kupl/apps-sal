def main():
    n = int(input())
    zo = set('10')

    strings = input().split()
    zer_num = 0
    start = '1'

    for s in strings:
        if s == '0':
            print(0)
            return
        elif (len(set(s) - zo) > 0) or ('1' in (s[1:])):
            start = s
        else:
            zer_num += len(s) - 1

    print(start + '0' * zer_num)


main()
