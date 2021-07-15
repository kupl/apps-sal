A, B, C = map(int, input().split())

rest = C - (A - B)

if rest > 0:
    print(rest)
else:
    print('0')
