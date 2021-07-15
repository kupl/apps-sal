class common_function():
    """
        1. よく使いそうで予め用意してあるものをまとめた
        2. よく使いそうな関数群をまとめた
    """
    def __init__(self):
        """
            1. 英字の一覧をリストに格納しておいた変数
        """
        self.sletter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.bletter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


    def combi(self, n:int, k:int, MOD=pow(10, 9) + 7):
        """
            mod の下での combination nCk を高速に求めるメソッド
            n が大きい場合(10^6)に使用する. 
            1回 nCk を求めるのに O(k) かかる.
        """
        k = min(k, n-k)
        numer = 1
        for i in range(n, n-k, -1):
            numer *= i
            numer %= MOD
        denom = 1
        for j in range(k, 0, -1):
            denom *= j
            denom %= MOD
        return (numer*(pow(denom, MOD-2, MOD)))%MOD


def main():
    common = common_function()
    X, Y = list(map(int, input().split()))
    if X <= 0 or Y <= 0 or (X + Y) % 3 != 0:
        print((0))
        return
    if Y > 2*X or X > 2*Y:
        print((0))
        return
    for i in range(X):
        two = i
        one = X-2*i
        if two + one*2 == Y:
            break
    ans = common.combi(two+one, one)
    print(ans)

def __starting_point():
    main()

__starting_point()
