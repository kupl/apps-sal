n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
mo = a.count(-1)
po = n - mo
ans = []
for i in range(m):
    a, b = [int(x) for x in input().split()]
    l = (b - a + 1)
    if l % 2:
        ans.append('0')
    elif po < l // 2 or mo < l // 2:
        ans.append('0')
    else:
        ans.append('1')
print('\n'.join(ans))
