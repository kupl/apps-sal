def work():
    s = input()
    a = [int(s[0]), int(s[1]), int(s[2])]
    b = [int(s[3]), int(s[4]), int(s[5])]
    if sum(a) == sum(b):
        print(0)
        return
    if sum(a) > sum(b):
        (a, b) = (b, a)
    a = sorted(a)
    b = sorted(b)
    ben = [9 - a[0], 9 - a[1], 9 - a[2], b[0], b[1], b[2]]
    ben = sorted(ben)[::-1]
    k = sum(b) - sum(a)
    t = 0
    i = 0
    while t < k:
        t += ben[i]
        i += 1
    print(i)
    return


work()
