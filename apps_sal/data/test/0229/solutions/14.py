n = int(input())
a = list(map(int, input().split()))
s = set()
for el in a:
    s.add(el)
    if len(s) > 3:
        break
if len(s) <= 2:
    print('YES')
elif len(s) > 3:
    print('NO')
else:
    sl = sorted(list(s))
    print('YES' if sl[0] + sl[2] == 2 * sl[1] else 'NO')
