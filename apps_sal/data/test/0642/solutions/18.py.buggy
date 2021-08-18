n, m = (int(x) for x in input().split())
if m == 0:
    print('YES')
    return
s = set()
for d in (int(x) for x in input().split()):
    s.add(d)
    if d == 1 or d == n:
        print('NO')
        return
    elif (d - 1) in s and ((d - 2) in s or (d + 1) in s):
        print('NO')
        return
    elif (d + 1) in s and (d + 2) in s:
        print('NO')
        return
print('YES')
