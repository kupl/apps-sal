n, m = list(map(int, input().split(' ')))
if m > n:
    n, m = m, n
# n > m

rowsGroups = n // 6
restRows = n % 6

count = 3 * rowsGroups * m

colsGroups = m // 6
restCols = m % 6

count += 3 * colsGroups * restRows

if not (restRows == 0 or restCols == 0):
    sn, sm = restRows, restCols
    if sm > sn:
        sn, sm = sm, sn

    if (sn, sm) == (1, 1):
        count += 0
    elif (sn, sm) == (5, 1):
        count += 2
    elif (sn, sm) == (4, 2):
        count += 4
    elif (sn, sm) == (5, 2):
        count += 5
    elif (sn, sm) == (3, 3):
        count += 4
    elif (sn, sm) == (4, 3):
        count += 6
    elif (sn, sm) == (5, 3):
        count += 7
    elif (sn, sm) == (4, 4):
        count += 8
    elif (sn, sm) == (5, 4):
        count += 10
    elif (sn, sm) == (5, 5):
        count += 12
    elif (sn, sm) == (2, 1):
        if restRows == 2:
            if colsGroups >= 2 or (colsGroups == 1 and rowsGroups >= 1):
                count += 1
        elif restCols == 2:
            if rowsGroups >= 2 or (rowsGroups == 1 and colsGroups >= 1):
                count += 1
    elif (sn, sm) == (3, 1):
        if restRows == 3 and colsGroups >= 1:
            count += 1
        if restCols == 3 and rowsGroups >= 1:
            count += 1
    elif (sn, sm) == (4, 1):
        if restRows == 4 and colsGroups >= 1:
            count += 2
        elif restCols == 4 and rowsGroups >= 1:
            count += 2
        else:
            count += 1
    elif (sn, sm) == (2, 2):
        if rowsGroups >= 1 or colsGroups >= 1:
            count += 2
    elif (sn, sm) == (3, 2):
        if rowsGroups >= 1 or colsGroups >= 1:
            count += 3
        else:
            count += 2
    else:
        raise f'Unknown pair ({sn, sm})'

print(2 * count)
