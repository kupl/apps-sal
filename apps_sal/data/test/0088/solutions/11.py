a, b = list(map(int, input().split()))

maxL = 60
sol = 0

for l in range(1, maxL + 1):
    for p in range(1, l + 1):
        binYear = '1' * p + '0' + (l - p) * '1'
        # print(binYear)

        decYear = int(binYear, 2)

        if a <= decYear and decYear <= b:
            sol += 1

print(sol)
