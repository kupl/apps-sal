n = int(input())
s = input().strip()
xsmall = s.count('x')
xbig = s.count('X')
if xbig < xsmall:
    print((xsmall - xbig) // 2)
    print(s.replace('x', 'X', (xsmall - xbig) // 2))
else:
    print((xbig - xsmall) // 2)
    print(s.replace('X', 'x', (xbig - xsmall) // 2))
