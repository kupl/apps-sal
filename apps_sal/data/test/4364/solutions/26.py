s = input()
head = int(s[:2])
tail = int(s[2:])

is_mmyy = False
is_yymm = False

if 1 <= head <= 12:
    is_mmyy = True

if 1 <= tail <= 12:
    is_yymm = True

if is_yymm and is_mmyy:
    print('AMBIGUOUS')
elif is_yymm:
    print('YYMM')
elif is_mmyy:
    print('MMYY')
else:
    print('NA')
