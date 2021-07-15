r, g, b = map(int, input().split())
judged = int(str(g) + str(b))
if judged % 4 == 0:
    print('YES')
else:
    print('NO')
