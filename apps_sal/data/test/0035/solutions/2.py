def check_flag(flag, n, m):
    if n % 3 > 0 and m % 3 > 0:
        return False
    if n % 3 == 0:
        nrows = int(n / 3)
        set1 = set(''.join(flag[:nrows]))
        set2 = set(''.join(flag[nrows:2 * nrows]))
        set3 = set(''.join(flag[2 * nrows:]))
        if len(set1) + len(set2) + len(set3) == 3 and len(set1.union(set2.union(set3))) == 3:
            return True
    if m % 3 == 0:
        ncols = int(m / 3)
        set1 = set(''.join([row[:ncols] for row in flag]))
        set2 = set(''.join([row[ncols:2 * ncols] for row in flag]))
        set3 = set(''.join([row[2 * ncols:] for row in flag]))
        if len(set1) + len(set2) + len(set3) == 3 and len(set1.union(set2.union(set3))) == 3:
            return True
    return False


(n, m) = [int(i) for i in input().strip(' ').split(' ')]
flag = []
for _ in range(n):
    flag.append(input().strip(' '))
if check_flag(flag, n, m):
    print('YES')
else:
    print('NO')
