def gen(i, cur):
    nonlocal dvs, used
    if i == len(kk):
        if (ohne != 1 or cur != 1) and (ok or not used[cur * ohne]):
            dvs.append(cur * ohne)
        return
    gen(i + 1, cur)
    for j in range(kk[i]):
        cur *= pp[i]
        gen(i + 1, cur)


gans = []
for _ in range(int(input())):
    n = int(input())
    pp = []
    kk = []
    i = 2
    cnt = []
    while i * i <= n:
        if n % i == 0:
            pp.append(i)
            kk.append(0)
            while n % i == 0:
                kk[-1] += 1
                n //= i
        i += 1
    if n != 1:
        pp.append(n)
        kk.append(1)
    dvs = []
    ohne = 1
    ok = True
    gen(0, 1)
    if len(pp) == 1:
        gans.append(' '.join(map(str, dvs)))
        gans.append(str(0))
    elif len(pp) == 2 and kk[0] == kk[1] == 1:
        gans.append(' '.join(map(str, dvs)))
        gans.append(str(1))
    elif len(pp) == 2:
        used = dict()
        for i in range(len(dvs)):
            used[dvs[i]] = False
        ans = []
        ok = False
        used[pp[0] * pp[1]] = True
        aaa = [pp[0] * pp[1]]
        if kk[0] > 1:
            used[pp[0] * pp[0] * pp[1]] = True
            aaa.append(pp[0] * pp[0] * pp[1])
        else:
            used[pp[0] * pp[1] * pp[1]] = True
            aaa.append(pp[0] * pp[1] * pp[1])
        for i in range(len(pp)):
            dvs = []
            ans.append(aaa[i])
            kk[i] -= 1
            ohne = pp[i]
            gen(0, 1)
            for j in range(len(dvs)):
                used[dvs[j]] = True
                ans.append(dvs[j])
        gans.append(' '.join(map(str, ans)))
        gans.append(str(0))
    else:
        used = dict()
        for i in range(len(dvs)):
            used[dvs[i]] = False
        ans = []
        ok = False
        for i in range(len(pp)):
            used[pp[i - 1] * pp[i]] = True
        for i in range(len(pp)):
            dvs = []
            ans.append(pp[i - 1] * pp[i])
            kk[i] -= 1
            ohne = pp[i]
            gen(0, 1)
            for j in range(len(dvs)):
                used[dvs[j]] = True
                ans.append(dvs[j])
        gans.append(' '.join(map(str, ans)))
        gans.append(str(0))
print('\n'.join(gans))

