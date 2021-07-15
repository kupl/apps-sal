def main():
    K = int(input())
    N = 50

    q, r = divmod(K, N)
    a = [x + q for x in range(N)]  # 全体への操作をqセットでき、1セットあたり全体1増加
    for i in range(N):
        if i < r:
            a[i] += N
            a[i] -= r - 1
        else:
            a[i] -= r

    print(N)
    print((*a))


def __starting_point():
    main()

# 0,1,2,...,N-1
# N,0,1,2,...,N-2
# N-1,N,0,1,2,...,N-3
# ...
# ...0,1
# ...N,0
# ...N-1,N

# 毎回どこかが0になり、そこをN加算し、他を1引く
# 全体を一回ずつ操作するとN加算してN-1引くので、1増える

__starting_point()
