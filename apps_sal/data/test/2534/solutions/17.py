def __starting_point():
    ROWS, COLS = list(map(int, input().strip().split()))

    giftCost = set()

    matrix = []
    minRow = []
    for i in range(ROWS):
        arr = list(map(int, input().strip().split()))
        minRow.append( min(arr) )
        matrix.append(arr)

    maxCol = []
    for j in range(COLS):
        maxi = -1
        for i in range(ROWS):
            maxi = max(maxi, matrix[i][j])
        maxCol.append( maxi )

    for i in range(ROWS):
        n = minRow[i]
        if n in giftCost:
            continue
        for j in range(COLS):
            if matrix[i][j] == n and maxCol[j] == n:
                giftCost.add(n)
            if len(giftCost) > 1:
                break
        if len(giftCost) > 1:
            break

    if len(giftCost) == 1:
        for n in giftCost:
            print(n)
    else:
        print("GUESS")
__starting_point()
