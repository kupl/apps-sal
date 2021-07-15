import sys

def main():
    N,*S = map(int, open(0).read().split())
    S = sorted(S)

    g = [S.pop(-1)]

    for gen in range(N):
        tmp = []
        for p in g[:2**gen]:
            while S:
                s = S.pop(-1)
                if p > s:
                    g.append(s)
                    break
                else:
                    tmp.append(s)
            else:
                print('No')
                return
        S.extend(tmp[::-1])
        g.sort(reverse=True)
    print('Yes')

def __starting_point():
    main()
__starting_point()
