e = str(input())
a, b, c = e.index('+'), e.index('=') - e.index('+') - 1, len(e) - e.index('=') - 1
if a + b == c:
    print(e)
elif a > 1 and a - 1 + b == c + 1:
    print("|" * (a - 1) + '+' + "|" * b + '=' + "|" * (c + 1))
elif b > 1 and a + b - 1 == c + 1:
    print("|" * a + '+' + "|" * (b - 1) + '=' + "|" * (c + 1))
elif c > 1 and a + 1 + b == c - 1:
    print("|" * (a + 1) + '+' + "|" * b + '=' + "|" * (c - 1))
else:
    print("Impossible")
