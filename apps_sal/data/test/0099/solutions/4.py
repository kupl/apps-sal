(s, r, m, n) = list(map(int, input().split()))
bad = set(map(int, input().split()))
cnt = 0
if abs(s) > m:
    print(0)
elif s == 0:
    if 0 in bad:
        print(0)
    else:
        print('inf')
elif r == 0 and s != 0:
    if 0 in bad or m < 0:
        if s in bad:
            print(0)
        else:
            print(1)
    else:
        print('inf')
elif r == 1:
    if s in bad:
        print(0)
    else:
        print('inf')
elif r == -1:
    if s in bad and -s in bad:
        print(0)
    else:
        print('inf')
elif -1 <= r <= 1 and r != 0:
    print('inf')
else:
    while abs(s) <= m:
        if s not in bad:
            cnt += 1
        s *= r
    print(cnt)
