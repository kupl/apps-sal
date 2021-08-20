(n, m) = map(int, input().split())
if m == 0:
    print('YES')
else:
    t = list(map(int, input().split()))
    t.sort()
    if t[0] == 1 or t[-1] == n:
        print('NO')
    else:
        k = s = 0
        for i in t:
            if i == k:
                s += 1
                k += 1
                if s > 1:
                    s = -1
                    break
            else:
                (k, s) = (i + 1, 0)
        print('YNEOS'[s == -1::2])
