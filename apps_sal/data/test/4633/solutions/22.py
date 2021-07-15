
t = int(input())
def dgt_sum(num):
    return sum([int(x) for x in str(num)])

def clps(val, left=0):
    if len(str(val)) == 1:
        return 1, left + 1


    return int(str(val)[:-1]) + 1, left + 1


def solve(n, s):
    n_str =str(n)
    _s = 0
    target = n
    for i, d in enumerate(n_str):
        d = int(d)
        _s+=d
        if _s > s:
            cl = int(n_str[:i+1]), 0
            while dgt_sum(cl[0]) > s:
                cl = clps(*cl)

            target = cl[0] * pow(10, cl[1] + len(n_str) -i-1)
            break

    return target - n



for _ in range(t):
    n,s = [int(x) for x in input().split(' ')]
    print(solve(n,s))
