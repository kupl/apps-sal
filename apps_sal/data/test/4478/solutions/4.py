n = int(input())
cl = set()
dic = {}
for i in range(n):
    m = int(input())
    s = list(map(int, input().split()))
    t = []
    sm = sum(s)
    for x in range(m):
        a = sm - s[x]
        if a in cl:
            print('YES')
            print('{} {}'.format(i + 1, x + 1))
            print('{} {}'.format(dic[a][0], dic[a][1]))
            return
        dic.update({a: (i + 1, x + 1)})
        t.append(a)
    for x in set(t):
        cl.add(x)


print('NO')
