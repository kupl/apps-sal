
def __starting_point():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    freq = {}
    for v in a:
        freq[v] = freq.get(v, 0) + 1
    res = 0
    cfreq = {}
    for v in a:
        y = v ^ x
        #t = freq[v] - cfreq.get(v, 0)
        cfreq[v] = cfreq.get(v, 0) + 1
        if y in freq:
            res += freq[y] - cfreq.get(y, 0)
    print(res)


__starting_point()
