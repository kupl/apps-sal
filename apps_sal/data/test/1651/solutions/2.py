(s, p) = map(int, input().split())
n = (s + (s ** 2 - 4 * p) ** (1 / 2)) / 2
if n % 1 == 0 and n > 0:
    if s - n > 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')
