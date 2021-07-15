def solve(bs, gs):
    bs.sort()
    gs.sort()
    ret = 0
    while gs and bs:
        if -2 < gs[-1] - bs[-1] < 2:
            ret += 1
            bs.pop()
            gs.pop()
        elif bs[-1] > gs[-1]:
            bs.pop()
        else:
            gs.pop()
    return ret
    
def __starting_point():
    input()
    bs = list(map(int, input().split()))
    input()
    gs = list(map(int, input().split()))
    print(solve(bs, gs))
__starting_point()
