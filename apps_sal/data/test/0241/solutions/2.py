(n, m, min_, max_) = list(map(int, input().split()))
l = sorted(list(map(int, input().split())))
if l[0] < min_ or l[-1] > max_:
    print('Incorrect')
else:
    if l[-1] < max_:
        l.append(max_)
    if l[0] > min_:
        l.append(min_)
    if len(l) <= n:
        print('Correct')
    else:
        print('Incorrect')
