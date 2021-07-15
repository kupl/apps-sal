for t in range(int(input())):
    s = 0
    n = input()
    s += 9 * (len(n) - 1)
    if int(n) >= int(n[0] * len(n)):
        s += int(n[0])
    else:
        s += int(n[0]) - 1
    print(s)

