n = int(input())
a = input()
opp = ['UD', 'DU', 'LR', 'RL']

c1 = None
c2 = None

cnt = 0

for i in range(n):
    if c1 is None:
        c1 = a[i]
    elif c1 == a[i] and c2 is None:
        continue
    elif c1 != a[i] and c2 is None:
        if c1 + a[i] in opp:
            cnt += 1
            c1 = a[i]
            c2 = None
        else:
            c2 = a[i]
    elif c1 is not None and c2 is not None and (c1 == a[i] or c2 == a[i]):
        continue
    elif c1 is not None and c2 is not None and (c1 != a[i] and c2 != a[i]):
        cnt += 1
        c1 = a[i]
        c2 = None

print(cnt + 1)
