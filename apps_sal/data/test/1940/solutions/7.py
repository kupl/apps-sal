(n, k) = list(map(int, input().split()))
ws = list((int(x) for x in input().split()))
result = 0
free_pocket = False
for w in ws:
    needed_pockets = (w + k - 1) // k
    if needed_pockets % 2 == 0:
        result += needed_pockets // 2
    else:
        if free_pocket:
            result += (needed_pockets - 1) // 2
        else:
            result += (needed_pockets + 1) // 2
        free_pocket = not free_pocket
print(result)
