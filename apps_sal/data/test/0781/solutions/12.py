valid = True
for i in range(8):
    line = input()
    if line != 'WBWBWBWB' and line != 'BWBWBWBW':
        valid = False
if valid:
    print('YES')
else:
    print('NO')
