s = input()
l = s[-1]
s = int(s[:-1])
ez = '=fedabc'
if (s%4 == 3 or s%4 == 0):
    s -= 2
if s%4 == 1:
    print(16*(s//4)+ez.index(l))
elif s%4 == 2:
    print(7+16*(s//4)+ez.index(l))

