s = input()

if '+' in s:
    index = s.index('+')
    print((int(s[:index])+int(s[index+1:])))
else:
    index = s.index('-')
    print((int(s[:index])-int(s[index+1:])))

