s = list(input())
L = ['A', 'E', 'F', 'H', 'I', 'K', 'L', 'M', 'N', 'T', 'V', 'W', 'X', 'Y', 'Z']
C = ['B', 'C', 'D', 'G', 'J', 'O', 'P', 'Q', 'R', 'S', 'U']
total = 0
for i in s:
    if i in L:
        total += 1
    if i in C:
        total += 2
if total == len(s) or total == len(s) * 2:
    print('YES')
else:
    print('NO')
