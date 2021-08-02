k = int(input())
c = [0] * 9
for i in range(4):
    a = input().strip()
    for i in a:
        if i != '.':
            c[int(i) - 1] += 1
if max(c) <= 2 * k:
    print('YES')
else:
    print('NO')
