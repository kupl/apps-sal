def check(table):
    n = len(table)
    m = len(table[0])
    bits = [[table[i][j] == j+1 for j in range(m)] for i in range(n)]
    for row in bits:
        if row.count(False) > 2:
            return False
    return True

n,m =list(map(int, input().split()))
table = [list(map(int, input().split())) for i in range(n)]
for i in range(m-1):
    for j in range(i,m):
        _table = [table[i][:] for i in range(n)]
        for k in range(n):
            _table[k][i], _table[k][j] = _table[k][j],_table[k][i]
        if check(_table):
            print('YES')
            return
if check(table):
    print('YES')
    return

print('NO')


