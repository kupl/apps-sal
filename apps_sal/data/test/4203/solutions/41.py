def main():
    s = input()
    len_s = len(s)
    if s[0] == 'A' and s[2:-1].count('C') == 1 and (sum((s[i].islower() for i in range(len_s))) == len_s - 2):
        print('AC')
    else:
        print('WA')


main()
