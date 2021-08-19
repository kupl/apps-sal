class Solution:

    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        mod = 10 ** 9 + 7

        def memo(f):
            dic = {}

            def f_alt(*args):
                if args not in dic:
                    dic[args] = f(*args)
                return dic[args]
            return f_alt

        @memo
        def play(N, L):
            if L == 0:
                return 1 if N == 0 else 0
            if N > L:
                return 0
            return (N * play(N - 1, L - 1) + max(0, N - K) * play(N, L - 1)) % mod
        return play(N, L)
