class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:

        dic = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        num = 0
        num_c = 0
        num_k = 0

        freq = [0] * 5

        if not croakOfFrogs[0] == 'c':
            return -1

        for ch in croakOfFrogs:
            if 'c' == ch:
                if num_k == 0:
                    num_c += 1
                else:
                    num_k -= 1
                num = max(num_c, num)
            if 'k' == ch:
                num_k += 1

        for ch in croakOfFrogs:
            freq[dic[ch]] += 1

            for idx in range(1, 5):
                if freq[idx] > freq[idx - 1]:
                    return -1

        for idx in range(1, 5):
            if not freq[idx] == freq[idx - 1]:
                return -1

        return num
