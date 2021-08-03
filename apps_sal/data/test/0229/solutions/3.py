n = int(input())
ip = list(map(int, input().split()))
count = 0
used = []
for i in ip:
    if i not in used and count < 5:
        used.append(i)
        count += 1
if count <= 2:
    print('YES')
elif count > 3:
    print('NO')
else:
    used = sorted(used)
    if used[1] - used[0] == used[2] - used[1]:
        print('YES')
    else:
        print('NO')
