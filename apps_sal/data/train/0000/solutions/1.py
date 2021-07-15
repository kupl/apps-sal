k = int(input())
for i in range(k):
    is_t = set()
    a = dict()
    a['00'] = []
    a['11'] = []
    a['01'] = []
    a['10'] = []    
    n = int(input())
    s = []
    for i in range(n):
        b = input()
        a[b[0] + b[-1]].append(i)
        s.append(b)
        is_t.add(b)
    c = len(a['10'])
    d = len(a['01'])
    if c + d == 0:
        if len(a['00']) == 0 or len(a['11']) == 0:
            print(0)
        else:
            print(-1)
    elif c > d:
        ans = []
        i = 0
        m = (d + c) // 2
        while d != m and i < len(a['10']):
            s1 = s[a['10'][i]]
            if s1[::-1] not in is_t:
                d += 1
                ans.append(a['10'][i] + 1)
            i += 1
        if d != m:
            print(-1)
        else:
            print(len(ans))
            print(*ans)
    else:
        ans = []
        i = 0
        m = (d + c) // 2
        while c != m and i < len(a['01']):
            s1 = s[a['01'][i]]
            if s1[::-1] not in is_t:
                c += 1
                ans.append(a['01'][i] + 1)
            i += 1
        if c != m:
            print(-1)
        else:
            print(len(ans))
            print(*ans)

