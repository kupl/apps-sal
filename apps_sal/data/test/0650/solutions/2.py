lin = set(list('AEFHIKLMNTVWXYZ'))
cur = set(list('BCDGJOPQRSU'))
s = set(list(input()))
if lin | s == lin or cur | s == cur:
    print('YES')
else:
    print('NO')
