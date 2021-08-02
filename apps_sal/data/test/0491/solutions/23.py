def __starting_point():
    data = input()
    if int(data) >= 0:
        print(data)
    elif len(data) == 2:
        print('0')
    else:
        n = data[1:]
        l1 = n[:len(n) - 1]
        l2 = n[:len(n) - 2] + n[len(n) - 1:]
        ans = min(int(l1), int(l2))
        ans *= -1
        print(ans)


__starting_point()
