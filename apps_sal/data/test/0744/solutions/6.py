n = int(input())
s = input()

k1 = 0
k2 = 0
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        if s[x] == 'S':
            k1 += 1
        else:
            k2 += 1
if k1 > k2:
    print('YES')
else:
    print('NO')

