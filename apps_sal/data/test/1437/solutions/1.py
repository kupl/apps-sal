s = input()
ans = 1
for x in s:
    if 48 <= ord(x) <= 57:
        now = int(x)
    elif 65 <= ord(x) <= 90:
        now = ord(x) - 55
    elif 97 <= ord(x) <= 122:
        now = ord(x) - 61
    elif x == '-':
        now = 62
    else:
        now = 63
    for i in range(6):
        if now & 2 ** i == 0:
            ans = ans * 3 % (10 ** 9 + 7)
print(ans)
