s = input()
red = 0
blue = 0
for i in s:
    if i == '0':
        red += 1
    else:
        blue += 1
print(red + blue - abs(red - blue))
