for _ in range(int(input())):
    s = input()
    print(s[s.find('1'):s.rfind('1')].count('0'))
