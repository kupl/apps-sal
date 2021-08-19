#!/usr/bin/env python3


def main():
    from collections import deque

    def prime_factorization_list(n: int):
        """
        入力された整数nを素因数分解し，素因数が列挙されたリストで返却
        Parameters
        ----------
        n : int
            素因数分解したい整数
        Returns
        -------
        prime_factorization_lst : lst
            [素因数]の形で素因数が列挙された素因数分解結果
        """
        fct = []  # prime factor
        b = 2     # base factor
        while b * b <= n:
            while n % b == 0:
                n //= b
                fct.append(b)
            b += 1
        if n > 1:
            fct.append(n)
        return fct

    N = int(input())

    q = deque(prime_factorization_list(N))
    memo = []
    while q:
        p = q.popleft()
        res = p
        while res in memo and q:
            can = q.popleft()
            if can == p:
                res *= can
            else:
                res = can
                break
        if res not in memo:
            memo.append(res)
    print((len(memo)))


def __starting_point():
    main()


__starting_point()
