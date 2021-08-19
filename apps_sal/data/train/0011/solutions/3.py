t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    fa, fd, fs, fw = [0], [0], [0], [0]
    ba, bd, bs, bw = [0], [0], [0], [0]
    cur = [0, 0]
    for i in range(n):
        if s[i] == "A":
            cur[0] -= 1

        elif s[i] == "D":
            cur[0] += 1

        elif s[i] == "S":
            cur[1] -= 1

        elif s[i] == "W":
            cur[1] += 1

        fa.append(min(fa[-1], cur[0]))
        fd.append(max(fd[-1], cur[0]))
        fs.append(min(fs[-1], cur[1]))
        fw.append(max(fw[-1], cur[1]))

    h = fd[-1] - fa[-1]
    v = fw[-1] - fs[-1]
    area = (h + 1) * (v + 1)

    cur = [0, 0]
    for i in range(n - 1, -1, -1):
        if s[i] == "D":
            cur[0] -= 1
        elif s[i] == "A":
            cur[0] += 1
        elif s[i] == "W":
            cur[1] -= 1
        elif s[i] == "S":
            cur[1] += 1

        ba.append(min(ba[-1], cur[0]))
        bd.append(max(bd[-1], cur[0]))
        bs.append(min(bs[-1], cur[1]))
        bw.append(max(bw[-1], cur[1]))

    ba.reverse()
    bd.reverse()
    bs.reverse()
    bw.reverse()

    #print(fa, fd, fs, fw)
    #print(ba, bd, bs, bw)

    hok, vok = False, False
    for i in range(1, n):
        #print(n, i)
        if fd[i] - fa[i] < h and abs(bd[i] - ba[i]) < h:
            hok = True
        if fw[i] - fs[i] < v and abs(bw[i] - bs[i]) < v:
            vok = True

    if hok:
        area = min(area, h * (v + 1))
    if vok:
        area = min(area, v * (h + 1))
    print(area)
