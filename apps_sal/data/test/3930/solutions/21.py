(n, k) = map(int, input().split())
qw = [int(i) for i in input().split()]
q = 1
c = 0
for i in range(50):
    summ = 0
    er = {q: 1}
    for u in qw:
        summ += u
        if summ in er:
            c += er[summ]
        if summ + q in er:
            er[summ + q] += 1
        else:
            er[summ + q] = 1
    q *= k
if k == 1:
    print(c // 50)
elif k == -1:
    print(c // 25)
else:
    print(c)
