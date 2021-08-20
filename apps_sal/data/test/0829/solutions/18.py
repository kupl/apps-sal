n = int(input())
s = input()
ones = s.count('1')
zeros = s.count('0')
if ones != zeros:
    print(1)
    print(s)
else:
    print(2)
    print(s[0], s[1:])
