s = input().strip()
if s[0].isupper():
    print(s)
else:
    b = s[0].swapcase()
    print(b + s[1:])
