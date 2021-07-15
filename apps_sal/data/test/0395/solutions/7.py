a = [int(i) for i in input().split()]
ans = False
for i in range(65):
    m = bin(i)[2:].zfill(6)
    if m.count('1') == 3:
        q = sum([a[z] for z in range(6) if m[z] == '1'])
        if q * 2 == sum(a):
            ans = True
            break
if ans:
    print('YES')
else:
    print('NO')
