def main():
    s = input()
    c = s.count('VK')
    if s.find('VVV') >= 0 or s.find('KKK') >= 0 or s[:2] == 'KK' or (s[-2:] == 'VV'):
        c += 1
    print(c)


main()
