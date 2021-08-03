s, c = input().split('=')
a, b = s.split('+')
a, b, c = list(map(len, [a, b, c]))

if a + b != c:
    if a > 1 and a - 1 + b == c + 1:
        a -= 1
        c += 1
    elif b > 1 and a + b - 1 == c + 1:
        b -= 1
        c += 1
    elif c > 1 and a + 1 + b == c - 1:
        c -= 1
        a += 1
    else:
        print("Impossible")
        return
print("|" * a + "+" + "|" * b + "=" + "|" * c)
