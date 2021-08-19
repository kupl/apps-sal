a = input()
b = input()
a_ones = [0 for i in range(len(a) + 2)]
a_zeros = [0 for i in range(len(a) + 2)]
counter1 = 0
counter0 = 0
total = 0
ones = 0
zeros = 0
la = len(a)
k = len(b) - la + 1
for i in range(la):
    if a[i] == '1':
        counter1 += 1
    else:
        counter0 += 1
    a_ones[i] = counter1
    a_zeros[i] = counter0
la -= 1
if len(a) * 2 <= len(b):
    for i in range(len(b)):
        if i < la:
            ones = a_ones[i]
            zeros = a_zeros[i]
            if b[i] == '0':
                total += ones
            else:
                total += zeros
        elif la <= i and i <= len(b) - la - 1:
            ones = a_ones[la]
            zeros = a_zeros[la]
            if b[i] == '0':
                total += ones
            else:
                total += zeros
        else:
            ones = a_ones[la] - a_ones[-len(b) + la + i]
            zeros = a_zeros[la] - a_zeros[-len(b) + la + i]
            if b[i] == '0':
                total += ones
            else:
                total += zeros
    print(total)
else:
    for i in range(len(b)):
        if i < len(b) - la - 1:
            ones = a_ones[i]
            zeros = a_zeros[i]
            if b[i] == '0':
                total += ones
            else:
                total += zeros
        elif i > la:
            ones = a_ones[la] - a_ones[-len(b) + la + i]
            zeros = a_zeros[la] - a_zeros[-len(b) + la + i]
            if b[i] == '0':
                total += ones
            else:
                total += zeros
        else:
            ones = a_ones[i + len(b) - la - k] - a_ones[i - k]
            zeros = a_zeros[i + len(b) - la - k] - a_zeros[i - k]
            if b[i] == '0':
                total += ones
            else:
                total += zeros
    print(total)
