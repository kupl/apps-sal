import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    ans = {N}
    if N > 2: ans |= {N-1}
    for i in range(2, N): #N-1の約数ならばsubtractした後1になる。もしくはpow(k, x) == Nの場合
        if i ** 2 > N: break
        if (N - 1) % i == 0:
            ans |= {i}
            if i ** 2 < N - 1:
                ans |= {(N - 1) // i}
        if N % i == 0:
            k = N
            while k % i == 0:
                k //= i
            if k % i == 1: ans |= {i}
            if i ** 2 < N:
                k = N
                while k % i == 0:
                    k //= i
                if k % i == 1: ans |= {i}
    print(len(ans))
    #print(ans)


    return 0

def __starting_point():
    solve()
__starting_point()
