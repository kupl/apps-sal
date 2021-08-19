from sys import stdin


def solve(tc):
    k = int(stdin.readline().strip())
    cmp = 9
    ndigit = 1
    while k > cmp * ndigit:
        k -= cmp * ndigit
        cmp *= 10
        ndigit += 1
    num = 10 ** (ndigit - 1) + (k - 1) // ndigit
    pos = (k - 1) % ndigit
    print(str(num)[pos])
    pass


LOCAL_TEST = not __debug__
if LOCAL_TEST:
    infile = __file__.split('.')[0] + '-test.in'
    stdin = open(infile, 'r')
tcs = int(stdin.readline().strip()) if LOCAL_TEST else 1
tc = 1
while tc <= tcs:
    solve(tc)
    tc += 1
