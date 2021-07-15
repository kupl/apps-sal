q = int(input())
for i in range(q):
    s = input()
    t = input()
    s = set(s)
    t = set(t)
    if len(s.intersection(t)) > 0:
        print('YES')
    else:
        print('NO')
