def buttons(m, n, Steps):
    if m == n:
        return Steps
    elif m % 2 == 0 and m > n:
        return buttons(m // 2, n, Steps + 1)
    elif m % 2 == 1 and m > n:
        return buttons((m + 1) // 2, n, Steps + 2)
    else:
        return Steps + (n - m)


[n, m] = (input()).split(' ')
print(buttons(int(m), int(n), 0))
