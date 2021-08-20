from sys import stdin, stdout


def compresswords(n, words):
    a = []
    for c in words[0]:
        a.append(c)
    for i in range(1, len(words)):
        lps = getlps(words[i])
        idx = getsuffixmatchIdx(a, words[i], lps)
        for j in range(idx, len(words[i])):
            a.append(words[i][j])
    return ''.join(a)


def getlps(w):
    lps = []
    lps.append(-1)
    for i in range(1, len(w)):
        c = w[i]
        idx = i - 1
        while idx >= 0 and w[lps[idx] + 1] != c:
            idx = lps[idx]
        if idx >= 0:
            idx = lps[idx] + 1
        lps.append(idx)
    return lps


def getsuffixmatchIdx(a, w, lps):
    widx = 0
    for i in range(max(0, len(a) - len(w)), len(a)):
        c = a[i]
        while widx >= 0 and w[widx] != c:
            widx -= 1
            if widx > 0:
                if lps[widx] >= 0:
                    widx = lps[widx] + 1
                else:
                    widx = 0
        widx += 1
    return widx


def __starting_point():
    n = int(stdin.readline())
    words = list(stdin.readline().split())
    if n != len(words):
        print('length not match')
    res = compresswords(n, words)
    print(res)


__starting_point()
