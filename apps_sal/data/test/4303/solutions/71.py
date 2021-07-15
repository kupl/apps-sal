def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]
    xs = [int(item) for item in input().split()]
    
    min_lr = 10**9
    min_rl = 10**9

    if N != K:
        for i in range(N-K+1):
            min_lr = min(min_lr, abs(xs[i]) + abs(xs[i+K-1] - xs[i]))
            min_rl = min(min_rl, abs(xs[i+K-1]) + abs(xs[i+K-1] - xs[i]))

        print((min(min_lr, min_rl)))
    elif N ==1:
        print((abs(xs[0])))
    else:
        print((min(abs(xs[0]) + abs(xs[N-1] - xs[0]), abs(xs[N-1]) + abs(xs[N-1] - xs[0]))))

def __starting_point():
    resolve()

__starting_point()
