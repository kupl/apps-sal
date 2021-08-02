N = str(int(input()))
total = 0
l = len(N) - 1
if l == 0:
    print(N)
else:
    for i in range(2**l):
        b = format(i, '0' + str(l) + 'b')
        subtotal = 0
        s = N[0]
        for j in range(len(b)):
            if int(b[j]):
                subtotal += int(s)
                s = N[j + 1]
            else:
                s += N[j + 1]

        subtotal += int(s)
        total += subtotal

    print(total)
