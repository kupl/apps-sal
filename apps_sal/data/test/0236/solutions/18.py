s = input().strip()

pearls = s.count("o")
links = s.count("-")

if not pearls or links % pearls == 0:
    print('YES')
else:
    print('NO')
