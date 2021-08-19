class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        dict = {}
        for num in arr:
            dict[num] = dict.get(num, 0) + 1

        size = len(arr) + 1
        counters = [[] for _ in range(size)]

        for num in dict:
            counters[dict[num]].append(num)

        result = len(dict)
        for i in range(size):
            if k == 0:
                break

            while counters[i] and k >= i:
                num = counters[i].pop()
                #del dict[num]
                result -= 1
                k -= i
        return result
