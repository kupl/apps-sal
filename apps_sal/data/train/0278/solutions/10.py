import numpy as np


class Solution:

    def largestMultipleOfThree(self, digits: List[int]) -> str:
        mod_gap = sum(digits) % 3
        if mod_gap == 0:
            answer = ''.join([str(i) for i in sorted(digits, reverse=True)])
        digits = np.array(digits)
        cond = digits % 3 == 0
        mult3 = digits[cond]
        non3 = digits[~cond]
        non3 = sorted(non3, reverse=True)
        non3 = np.array(non3)
        if mod_gap == 1:
            last_odd_idx = np.ravel(np.argwhere(non3 & 1))
            if len(last_odd_idx) > 0:
                last_odd_idx = last_odd_idx[-1]
                non3 = list(non3[:last_odd_idx]) + list(non3[last_odd_idx + 1:])
        elif mod_gap == 2:
            last_even_idx = np.ravel(np.argwhere(non3 % 2 == 0))
            if len(last_even_idx) > 0:
                last_even_idx = last_even_idx[-1]
                non3 = list(non3[:last_even_idx]) + list(non3[last_even_idx + 1:])
        if sum(non3) % 3 != 0:
            non3 = []
        answer = ''.join([str(int(i)) for i in sorted(np.concatenate([mult3, non3]), reverse=True)])
        while answer.startswith('0') and len(answer) > 1:
            answer = answer[1:]
        return answer
