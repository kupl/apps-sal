for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    s = input()
    cost = 0
    rowcost = a
    amchain = False
    for c in s:
        if c == '1':
            if not amchain and rowcost:
                amchain = True
                cost += min(rowcost, a)
        else:
            if amchain:
                amchain = False
                rowcost = b
            else:
                rowcost += b
    print(cost)
