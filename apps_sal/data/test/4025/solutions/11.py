a, b, c = map(int, input().split())
cnt = 0
cnt += min(a // 3, b // 2, c // 2)
a -= 3 * cnt
b -= 2 * cnt
c -= 2 * cnt
sas = 0
Q = [0, 1, 2, 0, 2, 1, 0]
for first_day in range(7):
    heh = 0
    aa, bb, cc = a, b, c
    W = [a, b, c]
    while W[Q[first_day]]:
        if Q[first_day] == 0:
            aa -= 1
        elif Q[first_day] == 1:
            bb -= 1
        else:
            cc -= 1
        first_day += 1
        heh += 1
        first_day %= 7
        W = [aa, bb, cc]
    sas = max(sas, heh)
print(sas + 7 * cnt)
