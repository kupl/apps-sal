from sys import stdin


def solve(tc):
    n = int(stdin.readline().strip())
    ans = n // 100
    n %= 100
    ans += n // 20
    n %= 20
    ans += n // 10
    n %= 10
    ans += n // 5
    n %= 5
    ans += n
    print(ans)
    pass


LOCAL_TEST = not __debug__
if LOCAL_TEST:
    infile = __file__.split('.')[0] + "-test.in"
    stdin = open(infile, 'r')

tcs = (int(stdin.readline().strip()) if LOCAL_TEST else 1)
tc = 1
while tc <= tcs:
    solve(tc)
    tc += 1
