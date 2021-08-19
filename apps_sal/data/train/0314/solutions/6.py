class Solution:

    def numSub(self, s: str) -> int:
        cont_one_count = 0
        one_sub = 0
        for char in s:
            if char == '1':
                cont_one_count += 1
            if char == '0':
                one_sub += cont_one_count * (cont_one_count + 1) / 2
                cont_one_count = 0
        one_sub += cont_one_count * (cont_one_count + 1) / 2
        return int(one_sub) % (10 ** 9 + 7)
