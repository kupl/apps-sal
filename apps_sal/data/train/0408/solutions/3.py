class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        min_diff = float('inf')
        n = len(arr)
        best = None
        counter = Counter(arr)
        count = 0
        partial_sum = sum(arr)
        sorting = sorted(counter, key=lambda x: -x)
        
        rounding = round(target / n)
        diff2 = abs(rounding * n - target)
        if rounding <= sorting[-1] and diff2 < min_diff:
            best = rounding
            min_diff = abs(rounding * n - target)

        for i in range(len(sorting)):
            num = sorting[i]
            count += counter[num]
            partial_sum -= num * counter[num]
            diff = abs(count * num + partial_sum - target)
            
            if diff <= min_diff:
                min_diff = diff
                best = num
                
            rounding = round((target - partial_sum) / count)
            if rounding > 0 and i < len(sorting) - 1 and rounding > sorting[i + 1] and rounding < sorting[0]:
                diff2 = abs(rounding * count + partial_sum - target)
                if diff2 < min_diff:
                    best = rounding
                    min_diff = diff2
            
        return best

