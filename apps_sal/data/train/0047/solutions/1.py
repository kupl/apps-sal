for i in range(int(input())):
    n, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    tot = 0
    small = 400000
    big = 0
    goingUp = True
    for i, val in enumerate(a):
        if goingUp:
            if val > big:
                big = val
            else:
                tot += big
                goingUp = False
                small = val
        else:
            if val < small:
                small = val
            else:
                tot -= small
                goingUp = True
                big = val
    if goingUp:
        tot += big
    print(tot)
