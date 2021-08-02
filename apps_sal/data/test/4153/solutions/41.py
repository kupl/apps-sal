S = input()

red = 0
blue = 0
for s in S:
    if s == '0':
        red += 1
    elif s == '1':
        blue += 1
print((min(red, blue) * 2))
