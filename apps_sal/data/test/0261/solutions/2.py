n = int(input())
s = input() + '.' * 600

has = False
for dif in range(1, 101):
    for st in range(100):
        if s[st] == s[st + dif] == s[st + 2 * dif] == s[st + 3 * dif] == s[st + 4 * dif] == '*':
            has = True

print('yes' if has else 'no')
