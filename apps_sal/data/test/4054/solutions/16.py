def solve(inp):
    # if inp=='2 4 6 8 10': return 1
    ar = list(map(int, inp.split(' ')))
    return min([ar[0], ar[1], ar[2] // 2, ar[3] // 7, ar[4] // 4])


inp = input()
print(solve(inp))
