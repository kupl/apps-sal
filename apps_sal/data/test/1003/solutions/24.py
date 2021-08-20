(lst, n, v) = (list(map(int, input().split(' '))), 0, 0)
if lst[0] == 1 and lst[1] == 1:
    print(2)
else:
    while lst[0] > v:
        n += 1
        if n == lst[1]:
            lst[0] += 1
            n = 0
        v += 1
    print(lst[0])
