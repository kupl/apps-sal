class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        length = len(arr)
        counter = {}
        for num in arr:
            try:
                counter[num] += 1
            except:
                counter[num] = 1

        array = sorted(list(counter.items()), key=lambda x: (-x[1], x[0]))
        # print(array)
        res = 0
        i = 0
        while res * 2 < length:
            res += array[i][1]
            i += 1
        return i
