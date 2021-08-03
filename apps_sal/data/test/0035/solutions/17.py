n, m = [int(el) for el in input().split()]
fl = [input().split() for i in range(n)]
fl1 = [['R' * m] for i in range(n // 3)] + [['G' * m]for i in range(n // 3)] + [['B' * m] for i in range(n // 3)]
fl2 = [['R' * m] for i in range(n // 3)] + [['B' * m] for i in range(n // 3)] + [['G' * m] for i in range(n // 3)]
fl3 = [['B' * m] for i in range(n // 3)] + [['G' * m] for i in range(n // 3)] + [['R' * m]for i in range(n // 3)]
fl4 = [['B' * m] for i in range(n // 3)] + [['R' * m]for i in range(n // 3)] + [['G' * m] for i in range(n // 3)]
fl5 = [['G' * m] for i in range(n // 3)] + [['R' * m]for i in range(n // 3)] + [['B' * m] for i in range(n // 3)]
fl6 = [['G' * m] for i in range(n // 3)] + [['B' * m]for i in range(n // 3)] + [['R' * m]for i in range(n // 3)]

fl7 = [['R' * (m // 3) + 'G' * (m // 3) + 'B' * (m // 3)] for i in range(n)]
fl8 = [['R' * (m // 3) + 'B' * (m // 3) + 'G' * (m // 3)] for i in range(n)]
fl9 = [['G' * (m // 3) + 'B' * (m // 3) + 'R' * (m // 3)] for i in range(n)]
fl10 = [['G' * (m // 3) + 'R' * (m // 3) + 'B' * (m // 3)] for i in range(n)]
fl11 = [['B' * (m // 3) + 'G' * (m // 3) + 'R' * (m // 3)] for i in range(n)]
fl12 = [['B' * (m // 3) + 'R' * (m // 3) + 'G' * (m // 3)] for i in range(n)]

if fl == fl1 or fl == fl2 or fl == fl3 or fl == fl4 or fl == fl5 or fl == fl6 or fl == fl7 or fl == fl8 or fl == fl9 or fl == fl10 or fl == fl11 or fl == fl12:
    print('YES')
else:
    print('NO')
