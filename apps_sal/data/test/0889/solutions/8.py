def sa(a, b, c, d):
    if a == b == c or a == b == d or a == c == d or (b == c == d):
        return True
    else:
        return False


tx = 0
t = []
for inpt in range(4):
    chars = []
    for char in input():
        chars.append(char)
    t.append(chars)
if sa(t[0][0], t[0][1], t[1][0], t[1][1]) or sa(t[0][1], t[0][2], t[1][1], t[1][2]) or sa(t[0][2], t[0][3], t[1][2], t[1][3]):
    print('YES')
elif sa(t[1][0], t[1][1], t[2][0], t[2][1]) or sa(t[1][1], t[1][2], t[2][1], t[2][2]) or sa(t[1][2], t[1][3], t[2][2], t[2][3]):
    print('YES')
elif sa(t[2][0], t[2][1], t[3][0], t[3][1]) or sa(t[2][1], t[2][2], t[3][1], t[3][2]) or sa(t[2][2], t[2][3], t[3][2], t[3][3]):
    print('YES')
else:
    print('NO')
