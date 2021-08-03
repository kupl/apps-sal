T = int(input())

w = [[-1, 0], [1, 0], [0, 1], [0, -1]]
mp = {'A': 0, 'D': 1, 'W': 2, 'S': 3}
while T > 0:
    T -= 1
    s = input()
    l = [0]
    r = [0]
    u = [0]
    d = [0]

    for dir in s[::-1]:
        l.append(l[-1])
        r.append(r[-1])
        u.append(u[-1])
        d.append(d[-1])
        if dir == 'A':
            l[-1] += 1
            if r[-1] > 0:
                r[-1] -= 1
        elif dir == 'D':
            r[-1] += 1
            if l[-1] > 0:
                l[-1] -= 1
        elif dir == 'S':
            d[-1] += 1
            if u[-1] > 0:
                u[-1] -= 1
        else:
            u[-1] += 1
            if d[-1] > 0:
                d[-1] -= 1

    l = l[::-1]
    r = r[::-1]
    u = u[::-1]
    d = d[::-1]

    x = 0
    y = 0
    ml = 0
    mr = 0
    mu = 0
    md = 0

    ans = (l[0] + r[0] + 1) * (u[0] + d[0] + 1)
    for i in range(len(s) + 1):
        mml = ml
        mmr = mr
        mmu = mu
        mmd = md
        for j in range(4):
            xx = x + w[j][0]
            yy = y + w[j][1]

            if xx < 0:
                ml = max(ml, -xx)
            if xx > 0:
                mr = max(mr, xx)
            if yy > 0:
                mu = max(mu, yy)
            if yy < 0:
                md = max(md, -yy)

            xx -= l[i]
            if xx < 0:
                ml = max(ml, -xx)
            xx += r[i] + l[i]
            if xx > 0:
                mr = max(mr, xx)
            yy -= d[i]
            if yy < 0:
                md = max(md, -yy)
            yy += u[i] + d[i]
            if yy > 0:
                mu = max(mu, yy)

            ans = min(ans, (ml + mr + 1) * (mu + md + 1))
            ml = mml
            mr = mmr
            mu = mmu
            md = mmd

        if i < len(s):
            x += w[mp[s[i]]][0]
            y += w[mp[s[i]]][1]
            if x < 0:
                ml = max(ml, -x)
            if x > 0:
                mr = max(mr, x)
            if y > 0:
                mu = max(mu, y)
            if y < 0:
                md = max(md, -y)

    print(ans)
