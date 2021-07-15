n, m = map(int, input().split())
f = list(map(int, input().split()))
b = list(map(int, input().split()))
s1 = set(f)
s2 = set(b)
ans = []
if s2 <= s1:
    d = {}
    for i in range(len(f)):
        if f[i] in d:
            d[f[i]].append(i + 1)
        else:
            d[f[i]] = [i + 1]
    for u in b:
        if u in d and len(d[u]) > 1:
            print('Ambiguity')
            break
        elif u in d:
            ans.append(d[u][0])
    else:
        print('Possible')
        print(' '.join(map(str, ans)))
else:
    print('Impossible')
