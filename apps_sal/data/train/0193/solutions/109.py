class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # count = Counter(arr)
        # count = sorted(count.items(), key=lambda item: item[1], reverse=1)
        # total = len(arr)
        # i = 0
        # res = set()
        # while total > len(arr) // 2:
        #     total -= count[i][1]
        #     res.add(count[i][0])
        #     i += 1
        # return res
        count = sorted(Counter(arr).values(), reverse=1)
        target = (len(arr)) // 2
        res = curr = 0
        for val in count:
            curr += val
            res += 1
            if curr >= target:
                break
        return res
