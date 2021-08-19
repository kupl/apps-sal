class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:

        def binary_code_of_length_k(k):
            if k == 1:
                return ['0', '1']
            t = binary_code_of_length_k(k - 1)
            return ['0' + i for i in t] + ['1' + i for i in t]
        k_string = binary_code_of_length_k(k)
        for i in k_string:
            if s.find(i) == -1:
                return False
        return True
