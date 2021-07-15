s = input()
minc = s[0]
for c in s:
    print('Ann' if minc < c else 'Mike')
    minc = min(c, minc)
