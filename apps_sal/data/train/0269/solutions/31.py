from typing import List
import re


class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        matches = re.finditer('(1)', ''.join(map(str, nums)))
        indexes = tuple([getattr(el, 'span')()[0] for el in matches])
        for i in range(1, len(indexes)):
            diff = indexes[i] - indexes[i - 1]
            if diff <= k:
                return False
        return True
