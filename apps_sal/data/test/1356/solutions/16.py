s = input()
c = s.count('a')
if c > len(s) // 2:
    print(len(s))
else:
    print(2 * c - 1)
