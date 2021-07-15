N = list(map(int, input().split()))
As = list(map(int, input().split()))

added = As[0] + As[1]
xored = 0
for A in As[2:]:
    xored ^= A

anded = added - xored
if anded % 2 == 1:
    print((-1))
    return
else:
    anded >>= 1

left_stones_l_A0 = '' # <= A[0] for sure.
left_stones_e_A0 = '' #not sure if this is <= A[0].
for i, (a, x) in enumerate(zip(format(anded, '045b'), format(xored, '045b'))):
    if x == '0':
        if a == '0':
            left_stones_l_A0 += '0'
            left_stones_e_A0 += '0'
        else:
            left_stones_l_A0 += '1'
            left_stones_e_A0 += '1'
    else:
        if a == '0':
            if int(left_stones_l_A0 + '1' + '1' * (44 - i), base = 2) <= As[0]:
                left_stones_l_A0 += '1'
            else:
                left_stones_l_A0 += '0'
            if int(left_stones_e_A0 + '1' + '1' * (44 - i), base = 2) <= As[0]:
                left_stones_e_A0 += '1'
                left_stones_l_A0 = left_stones_e_A0
            elif int(left_stones_e_A0 + '1' + '0' * (44 - i), base = 2) <= As[0]:
                left_stones_l_A0 = left_stones_e_A0 + '0'
                left_stones_e_A0 += '1'
            elif int(left_stones_e_A0 + '0' + '0' * (44 - i), base = 2) <= As[0]:
                left_stones_e_A0 += '0'
            else:
                left_stones_e_A0 = left_stones_l_A0
        else:
            print((-1))
            return

if int(left_stones_e_A0, base = 2) <= As[0]:
    ans = As[0] - int(left_stones_e_A0, base = 2)
else:
    ans = As[0] - int(left_stones_l_A0, base = 2)

if 0 <= ans < As[0]:
    print(ans)
else:
    print((-1))

