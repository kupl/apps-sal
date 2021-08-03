from math import log2

A, B = map(int, input().split())


def bitpos(x, digit=1):
    bit = x % (2**digit) // (2**(digit - 1))
    pos = x % (2**digit)
    return int(bit), pos


if B == 0:
    print(0)
    return
else:
    max_digit = int(log2(B)) + 1

xor = []
for i in range(max_digit):
    abit, apos = bitpos(A, i + 1)
    bbit, bpos = bitpos(B, i + 1)
    if i == 0:
        ar, br = A % 4, B % 4
        if (ar, br) in {(0, 1), (0, 2), (1, 1), (1, 2), (2, 3), (2, 0), (3, 3), (3, 0)}:
            xor.append('1')
            continue
        else:
            xor.append('0')
            continue

    if abit == 0 and bbit == 0:
        xor.append('0')
        continue
    elif abit == 1 and bbit == 0:
        if apos % 2 == 1:
            xor.append('1')
            continue
        else:
            xor.append('0')
            continue
    elif abit == 0 and bbit == 1:
        if bpos % 2 == 0:
            xor.append('1')
            continue
        else:
            xor.append('0')
            continue
    else:
        if abs(apos - bpos) % 2 == 1:
            xor.append('0')
            continue
        else:
            xor.append('1')
            continue
xor = xor[::-1]
print(int(''.join(xor), 2))
