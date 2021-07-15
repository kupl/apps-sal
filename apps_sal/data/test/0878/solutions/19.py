input()
a = ''.join(input().split())
res = 0
for aij in zip(a, a[1:]):
    if '1' in aij:
        res += sum(map(int, aij))
    else:
        print('Infinite')
        break
else:
    print('Finite')
    print(res - a.count('312'))

