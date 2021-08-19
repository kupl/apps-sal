def gen(digit, x, length, S):
    S.append(x)
    if length == 10:
        return
    if len(digit) == 1:
        for i in range(0, 10):
            next_x = x * 10 + i
            if i == digit[0]:
                gen(digit, next_x, length + 1, S)
            else:
                gen(digit + [i], next_x, length + 1, S)
    else:
        next_x1 = x * 10 + digit[0]
        next_x2 = x * 10 + digit[1]
        gen(digit, next_x1, length + 1, S)
        gen(digit, next_x2, length + 1, S)


S = []
for i in range(1, 10):
    gen([i], i, 1, S)
S = sorted(S)
x = int(input())
l = -1
u = len(S)
while u - l > 1:
    md = (u + l) // 2
    if x >= S[md]:
        l = md
    else:
        u = md
print(u)
