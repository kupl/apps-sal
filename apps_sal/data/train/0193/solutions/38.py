from collections import Counter


class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr) / 2
        count = 0
        dic = Counter(arr)
        for i in dic.most_common():
            half -= i[1]
            count += 1
            if half <= 0:
                return count
