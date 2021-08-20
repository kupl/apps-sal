from sys import stdin, stdout
for _ in range(int(input())):
    (n, m) = (int(x) for x in stdin.readline().split())
    a = [[] for i in range(n + 1)]
    b = []
    for i in range(m):
        (c, d) = (int(x) for x in stdin.readline().split())
        a[d].append(c)
        a[c].append(d)
        b.append([c, d])
    vis = [0] * (n + 1)
    co = []
    for i in range(1, n + 1):
        if vis[i] == 0:
            st = [i]
            vis[i] = 'e'
            e = 1
            o = 0
            while st:
                x = st.pop()
                for i in a[x]:
                    if vis[i] == 0:
                        if vis[x] == 'e':
                            vis[i] = 'o'
                            o += 1
                        else:
                            vis[i] = 'e'
                            e += 1
                        st.append(i)
            co.append([e, o])
    fl = 0
    for i in b:
        if vis[i[0]] == vis[i[1]]:
            stdout.write(str(0) + '\n')
            fl = 1
            break
    if fl == 0:
        k = []
        for i in range(len(co)):
            x = co[i][0]
            y = co[i][1]
            m = 1
            for i in range(x):
                m *= 2
                m %= 998244353
            ans = m
            m = 1
            for i in range(y):
                m *= 2
                m %= 998244353
            ans += m
            k.append(ans % 998244353)
        ans = 1
        for i in k:
            ans *= i
            ans %= 998244353
        stdout.write(str(ans) + '\n')
