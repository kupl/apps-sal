class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dict = {}
        for num in arr:
            dict[num] = dict.get(num, 0) + 1
        size = len(arr) + 1
        buckets = [[] for _ in range(size)]
        for (num, freqency) in list(dict.items()):
            buckets[freqency].append(num)
        result = len(dict)
        for i in range(size):
            if k == 0:
                break
            while buckets[i] and k >= i:
                num = buckets[i].pop()
                result -= 1
                k -= i
        return result
