from collections import defaultdict


class RollingHash(object):
    def __init__(self, S: str, MOD: int = 10 ** 9 + 7, BASE: int = 10 ** 5 + 7):
        self.S = S
        self.N = N = len(S)
        self.MOD = MOD
        self.BASE = BASE
        self.S_arr = [ord(x) for x in S]

        self.POWER = [1] * (N + 1)
        self.HASH = [0] * (N + 1)
        p, h = 1, 0
        for i in range(N):
            self.POWER[i + 1] = p = (p * BASE) % MOD
            self.HASH[i + 1] = h = (h * BASE + self.S_arr[i]) % MOD

    def hash(self, l: int, r: int):
        # get hash for S[l:r]
        _hash = self.HASH[r] - (self.HASH[l] * self.POWER[r - l] % self.MOD)
        if _hash < 0:
            _hash += self.MOD
        return _hash

# 汎用的な二分探索のテンプレ
# check_func(x) = true となるxの最小値を探索する
# left : check_func(x) = falseとなるx
# right: check_func(x) = true となるx
# search_max: check_func(x) = true となるxの"最大値"を探索する場合はTrue
# check_func: answer <= x であればcheck_func(x) = true となるような関数


def binary_search(left: int, right: int, check_func, search_max: bool = False):
    # ok と ng のどちらが大きいかわからないことを考慮
    while abs(right - left) > 1:
        mid = (left + right) // 2

        if check_func(mid) ^ search_max:
            right = mid
            # print(left, right, mid, 't')
        else:
            left = mid
            # print(left, right, mid, 'f')

    return left if search_max else right


def main():
    N = int(input())
    S = input()

    rs = RollingHash(S)

    # 長さLの部分文字列同士が、範囲を重ねず同じ文字列となる場合はTrue,
    # そうでない場合はFalseを返す関数
    def isOK(L):
        if L == 0:
            return True
        hash_to_left = defaultdict(list)
        for i in range(N - L + 1):
            _hash = rs.hash(i, i + L)
            # hashが衝突しても文字列が完全に一致するか分からないので、
            # 衝突した場合は文字列が完全に一致するか調べ、かつ
            # 文字列同士がSの中で重なるような範囲にない場合はOKとする
            for j in hash_to_left[_hash]:
                if j + L <= i and S[i:i + L] == S[j:j + L]:
                    return True
            hash_to_left[_hash].append(i)

        return False
    # 範囲が重ならないことが条件にあるので、答えは最大でもN // 2（文字列の長さの半分）となる。
    # ただし、二分探索する上で絶対に答えとならない範囲を含めたいので、
    # 探索範囲としてはN // 2 + 1 と、+1しておく。
    ans = binary_search(0, N // 2 + 1, isOK, search_max=True)
    print(ans)


def __starting_point():
    main()


__starting_point()
