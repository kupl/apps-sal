def solve(n):
    maxx = len(bin(n)[2:])
    if not maxx & 1:
        maxx -= 1
    while maxx > 1:
        beaut = int('1' * (maxx // 2 + 1) + '0' * (maxx // 2), 2)
        if n % beaut == 0:
            return beaut
        maxx -= 2
    return 1


print(solve(int(input())))
