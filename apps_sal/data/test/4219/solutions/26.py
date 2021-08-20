def main():
    N = int(input())
    A = [[] for i in range(N)]
    for i in range(N):
        a = int(input())
        for j in range(a):
            (x, y) = [int(b) for b in input().split(' ')]
            A[i].append([x - 1, str(y)])
    cand = []
    for i in range(2 ** N):
        honest_flag = True
        bit = list(pad_zero(format(i, 'b'), N))
        honests = [int(p) for (p, q) in enumerate(bit) if q == '1']
        for honest in honests:
            w = A[honest]
            for k in range(len(w)):
                if w[k][1] != bit[w[k][0]]:
                    honest_flag = False
        if honest_flag:
            cand.append(len(honests))
    print(max(cand))


def pad_zero(s, n):
    s = str(s)
    return ('0' * n + s)[-n:]


main()
