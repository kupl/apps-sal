'''
Created on 2020/08/31

@author: harurun
'''


def main():
    from itertools import combinations
    import sys
    pin = sys.stdin.readline
    pout = sys.stdout.write
    perr = sys.stderr.write

    N = int(pin())
    ans = 0
    d = [0] * 5
    for _ in [0] * N:
        S = pin()[:-1][0]
        if S == "M":
            d[0] += 1
        elif S == "A":
            d[1] += 1
        elif S == "R":
            d[2] += 1
        elif S == "C":
            d[3] += 1
        elif S == "H":
            d[4] += 1
    c = list(combinations([0, 1, 2, 3, 4], 3))
    for i in c:
        cnt = 1
        for j in list(i):
            cnt *= d[j]
        ans += cnt
    print(ans)
    return


main()
