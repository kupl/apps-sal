class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        newList = [(v, l) for v, l in zip(values, labels)]
        newList.sort(reverse=True)

        ans = 0
        i = 0
        labelCounter = defaultdict(int)
        for v, l in newList:
            if labelCounter[l] < use_limit:
                # print(v, l)
                ans += v
                i += 1
                labelCounter[l] += 1
                if i == num_wanted:
                    break
        return ans
