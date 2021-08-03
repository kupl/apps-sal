class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        n_hash = {}
        n_str = str(N)
        for c in n_str:
            n_hash[c] = n_hash.get(c, 0) + 1

        for i in range(0, 31):
            num = pow(2, i)
            if len(str(num)) > len(str(N)):
                return False
            n_num = {}
            for c in str(num):
                n_num[c] = n_num.get(c, 0) + 1
            n_exists = True
            for k in n_hash:
                if n_num.get(k) and n_num.get(k) == n_hash.get(k):
                    pass
                else:
                    n_exists = False
                    break
            if n_exists:
                return True
        return False
