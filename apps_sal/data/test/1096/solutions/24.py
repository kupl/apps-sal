s = input()
(a, b) = (s[0], s[1])
res = 8
if a == 'a' or a == 'h':
    res -= 3
    if b == '1' or b == '8':
        res -= 2
elif b == '1' or b == '8':
    res -= 3
    if a == 'a' or a == 'h':
        res -= 2
print(res)
