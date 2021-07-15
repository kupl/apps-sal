

a = input()
b = input()

if sorted(list(a)) == sorted(list(b)):
    print(b)
elif len(a) < len(b):
    print(''.join(sorted(a)[::-1]))
else:
    digits = {}
    for x in a:
        y = int(x)
        if y in digits:
            digits[y] += 1
        else:
            digits[y] = 1

    best = 0

    for i in range(len(b)):
        digits_cpy = dict(digits)
        all_present = True
        for j in range(i):
            b_j = int(b[j])
            if b_j in digits_cpy and digits_cpy[b_j] != 0:
                digits_cpy[b_j] -= 1
            else:
                all_present = False

        if not all_present:
            continue

        found = False
        change = 0
        for z in range(int(b[i]) - 1, -1, -1):
            if z in digits_cpy and digits_cpy[z] != 0:
                found = True
                change = z
                digits_cpy[z] -= 1
                break

        if not found:
            continue

        digits_left = []
        for key, val in list(digits_cpy.items()):
            digits_left += [key] * val

        result = list(b[:i]) + [change] + sorted(digits_left)[::-1]

        best = max([best, int(''.join(map(str, result)))])

    print(best)

