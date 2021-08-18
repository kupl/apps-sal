from sys import stdin


def solve(tc):
    n = int(stdin.readline().strip())
    seq = list(map(int, stdin.readline().split()))

    elems = []
    idxcnt = 0
    idx = dict()
    for i in range(n):
        if seq[i] not in idx:
            idx[seq[i]] = idxcnt
            idxcnt += 1
            elems.append([])
        elems[idx[seq[i]]].append(i)

    ans = 1
    for li in elems:
        ans = max(ans, len(li))

    m = len(elems)
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            cur = -1
            cnt = 0
            leni, lenj = len(elems[i]), len(elems[j])
            pi, pj = 0, 0
            while True:
                while pi < leni and elems[i][pi] < cur:
                    pi += 1

                if pi == leni:
                    break
                cur = elems[i][pi]
                cnt += 1
                pi += 1

                while pj < lenj and elems[j][pj] < cur:
                    pj += 1

                if pj == lenj:
                    break
                cur = elems[j][pj]
                cnt += 1
                pj += 1
            ans = max(ans, cnt)

    print(ans)


tc = 1
solve(tc)
