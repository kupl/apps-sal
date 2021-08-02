ward = list(map(int, input().split()))

ward_sorted = sorted(ward)

if (ward_sorted[0] == 5) & (ward_sorted[1] == 5) & (ward_sorted[2] == 7):
    print('YES')
else:
    print('NO')
