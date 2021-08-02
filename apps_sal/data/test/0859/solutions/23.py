s = input()
t = input()
a, b, c = 0, 0, 0
for item in s:
    if item == '+':
        a += 1
    else:
        a -= 1
for item in t:
    if item == '+':
        b += 1
    elif item == '-':
        b -= 1
    else:
        c += 1
if c < abs(a - b) or (c - abs(a - b)) % 2 == 1:
    print(0)
else:
    x = 0.5 ** c
    for i in range((c - abs(a - b)) // 2):
        x *= c - i
        x /= 1 + i
    print(x)
