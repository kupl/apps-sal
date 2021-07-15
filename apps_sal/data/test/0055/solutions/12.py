def solve(n, k):
    bn = binary(n)
    if k < len(bn):
        return 'No'

    cur_dec = len(bn)
    next_dec = cur_dec+1
    while True:
        if k < next_dec:
            dif = k - cur_dec
            bn = list(reversed(bn))
            for _ in range(dif):
                e = bn.pop()
                bn += [e-1, e-1]
            return 'Yes\n' + ' '.join(map(str,bn))
        cur_dec = next_dec
        cnt = bn.count(bn[-1])
        bn = bn[:-cnt] + [bn[-1]-1]*(cnt*2)
        next_dec = cur_dec+bn.count(bn[-1])



def binary(x):
    out = []
    for i in reversed(list(range(64+1))):
        if x >= 2**i:
            x -= 2**i
            out.append(i)
    return list(reversed(out))


def __starting_point():
    n, k = list(map(int, input().split()))
    print(solve(n, k))

__starting_point()
