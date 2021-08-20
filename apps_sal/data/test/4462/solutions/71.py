input()
(a, b1, b2, b4, r) = (list(map(int, input().split())), 0, 0, 0, 'NYoe s')
for i in a:
    if i % 2 != 0:
        b1 += 1
    elif i % 4 == 0:
        b4 += 1
    else:
        b2 += 1
print([r[b1 <= b4::2], r[b1 <= b4 + 1::2]][not b2])
