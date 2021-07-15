for t in range(int(input())):
    a = input()
    out = 9 * (len(a) - 1)
    for i in range(1, 10):
        if(int(a) >= int(str(i) * len(a))):
            out += 1
        else:
            break
    print(out)

