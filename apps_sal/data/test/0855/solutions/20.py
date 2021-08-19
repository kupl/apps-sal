from decimal import *
# print(getcontext())
Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
getcontext().prec = 25

k, a, b = [int(i) for i in input().split(" ")]
A = []
B = []
ap = 0
bp = 0
ac = a
bc = b
ah = []
bh = []
sh = []
alert = 0
for i in range(3):
    A.append(input())
for i in range(3):
    B.append(input())


def Alice_choice(i, j):
    return int((A[i - 1])[2 * j - 2])


def Bob_choice(i, j):
    return int((B[i - 1])[2 * j - 2])


if ac == bc + 1 or ac == bc - 2:
    ap += 1
    ah.append(ac)
    bh.append(bc)
    sh.append(1)
elif bc == ac + 1 or bc == ac - 2:
    bp += 1
    ah.append(ac)
    bh.append(bc)
    sh.append(-1)
else:
    ah.append(ac)
    bh.append(bc)
    sh.append(0)
q = 0
r = 0
for q in range(k - 1):
    temp_a = Alice_choice(ac, bc)
    temp_b = Bob_choice(ac, bc)
    ac = temp_a
    bc = temp_b
    if ac == bc + 1 or ac == bc - 2:
        ap += 1
        ah.append(ac)
        bh.append(bc)
        sh.append(1)
    elif bc == ac + 1 or bc == ac - 2:
        bp += 1
        ah.append(ac)
        bh.append(bc)
        sh.append(-1)
    else:
        ah.append(ac)
        bh.append(bc)
        sh.append(0)
    for r in range(q + 1):
        if ac == ah[r] and bc == bh[r]:
            alert = 1
            break
    if alert == 1:
        break
q += 1
period = q - r
score_pp = sh[r + 1:q + 1]
end = (k - len(sh)) % period
repeat = Decimal(k - len(sh) - end) / period
aadd = 0
badd = 0
for i in score_pp:
    if i == 1:
        aadd += 1
    elif i == -1:
        badd += 1
ap += aadd * repeat
bp += badd * repeat
for i in score_pp[:end]:
    if i == 1:
        ap += 1
    elif i == -1:
        bp += 1

print(ap, end=' ')
print(bp)

# print(ah)
# print(bh)
# print(sh)
# print(r,q)
# print(score_pp)
# print(period)
# print(end)
# print(repeat)
# print(aadd,badd)

# Time Limit Exceeded #
