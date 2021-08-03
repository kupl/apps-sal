m = int(input())
count5 = 1
n = 5
while count5 < m:
    n += 5
    tn = n
    while tn % 5 == 0:
        tn /= 5
        count5 += 1
if count5 == m:
    print(5)
    print(' '.join(map(str, range(n, n + 5))))
else:
    print(0)
