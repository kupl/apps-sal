def resolve():
    '''
    code here
    '''
    N = int(input())

    memo = [0 for _ in range(N+1)]
    memo[:2] = [2, 1]

    for i in range(2, N+1):
        memo[i] = memo[i-1] + memo[i-2]

    print((memo[N]))

def __starting_point():
    resolve()

__starting_point()
