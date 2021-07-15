s, start, finish = map(int, input().split())
tramsp, igorsp = map(int, input().split())
p, d = map(int, input().split())

if start == finish:
    print('0')
else:
    if p <= start and d == 1:
        t = (start - p) * tramsp
        nd = d
    elif p >= start and d == -1:
        t = (p - start) * tramsp
        nd = d
    elif p > start and d == 1:
        t = (2 * (s - p) + (p - start)) * tramsp
        nd = -1
    else:
        t = (2 * p + (start - p)) * tramsp
        nd = 1

    if start <= finish and nd == 1:
        t += (finish - start) * tramsp
    elif start >= finish and nd == -1:
        t += (start - finish) * tramsp
    elif start > finish and nd == 1:
        t += (2 * (s - start) + (start - finish)) * tramsp
    else:
        t += (2 * start + (finish - start)) * tramsp

    i = abs(start - finish) * igorsp

    print(min(t, i))
