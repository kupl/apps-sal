Ci = input()
Cj = input()

if Ci[0] == Cj[-1] and Ci[1] == Cj[-2] and Ci[2] == Cj[-3]:
    print('YES')
else:
    print('NO')
