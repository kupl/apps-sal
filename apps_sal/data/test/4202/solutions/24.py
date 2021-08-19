(L, R) = list(map(int, input().split()))
if L + 2019 > R:
    tmp = 10 ** 9
    for l in range(L, R):
        for r in range(l + 1, R + 1):
            if l * r % 2019 < tmp:
                tmp = l * r % 2019
    print(tmp)
else:
    print('0')
