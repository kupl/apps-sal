val = map(int, input().split())
check_count = 0
for i in val:
    if i not in [5, 7]:
        print('NO')
    if i == 5:
        check_count += 1
if check_count == 2:
    print('YES')
else:
    print('NO')
