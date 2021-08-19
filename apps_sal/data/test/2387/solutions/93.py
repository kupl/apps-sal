def main():
    # IMPORT MODULE
    #import sys

    # sys.setrecursionlimit(100000)
    #input=lambda :sys.stdin.readline().rstrip()

    # f_inf=float("inf")
    # MOD=10**9+7

    if 'get_ipython' in globals():
        # SAMPLE INPUT
        n = 4
        S = ['((()))', '((((((', '))))))', '()()()']

    else:
        # INPUT
        n = int(input())
        #a, b = map(int, input().split())
        S = [input() for _ in range(n)]

    # SUBMITION CODES HERE
    def CNT(A):
        tmp, Min = 0, 0
        for a in A:
            if a == '(':
                tmp += 1
            else:
                tmp -= 1
            Min = min(Min, tmp)
        return (-Min, tmp - Min)

    T = [CNT(s) for s in S]

    pls = []
    mis = []
    for l, r in T:
        if l <= r:
            pls.append((l, r))
        else:
            mis.append((l, r))

    pls.sort(key=lambda a: a[0])
    mis.sort(key=lambda a: a[1], reverse=True)
    total = pls + mis

    levl = 0
    for l, r in total:
        levl -= l
        if levl < 0:
            print('No')
            return
        levl += r

    print('Yes' if levl == 0 else 'No')


main()
