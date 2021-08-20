from collections import deque
import numpy as np
import sys
sysread = sys.stdin.readline
read = sys.stdin.read
sys.setrecursionlimit(10 ** 7)


def generate_inv(n, mod):
    """
    逆元行列
    n >= 2
    Note: mod must bwe a prime number
    """
    ret = [0, 1]
    for i in range(2, n + 1):
        next = -ret[mod % i] * (mod // i)
        next %= mod
        ret.append(next)
    return ret


def generate_comb_m_i(M, N, inv, mod):
    ret = [1, M]
    for i in range(2, N + 1):
        tmp = ret[-1] * (M - (i - 1)) * inv[i] % mod
        ret.append(tmp)
    return ret


def generate_p_N_i(N, mod):
    ret = [1]
    for i in range(1, N + 1):
        tmp = ret[-1] * (N - (i - 1)) % mod
        ret.append(tmp)
    return ret


def generate_p_mi_ni(M, N, mod):
    ret = deque([1])
    cache = deque([1])
    for i in range(1, N + 1):
        tmp = cache[0] * (M - N + i) % mod
        cache.appendleft(tmp)
        ret.appendleft(tmp ** 2 % mod)
    return ret


def run():
    (N, M) = map(int, input().split())
    mod = 10 ** 9 + 7
    inv = generate_inv(M, mod)
    comb_m_i = generate_comb_m_i(M, N, inv, mod)
    p_N_i = generate_p_N_i(N, mod)
    p_mi_ni = generate_p_mi_ni(M, N, mod)
    ret = p_mi_ni[0]
    arr01 = [-1, 1] * (N // 2 + 1)
    arr01 = arr01[:N + 1]
    comb_m_i = np.array(comb_m_i, dtype=np.int64)
    p_N_i = np.array(p_N_i, dtype=np.int64)
    p_mi_ni = np.array(p_mi_ni, dtype=np.int64)
    arr01 = np.array(arr01, dtype=np.int64)
    tmp = comb_m_i * p_N_i % mod
    tmp = tmp * p_mi_ni % mod
    tmp = tmp * arr01 % mod
    tmp = tmp[1:]
    sub = 0
    for val in tmp:
        sub += val
        sub %= mod
    ret -= sub
    ret %= mod
    print(ret)


def __starting_point():
    run()


__starting_point()
