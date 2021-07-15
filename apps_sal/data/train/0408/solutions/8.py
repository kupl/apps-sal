class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        total = sum(arr)
        if total <= target:
            return max(arr)
        
        arr = sorted(arr)

        min_num = target // len(arr)
        if min_num <= arr[0]:
            below = len(arr) * min_num
            above = len(arr) * (min_num + 1)

            if abs(target - below) <= abs(target - above):
                return min_num
            else:
                return min_num + 1
        return self.findBestValue(arr[1:], target - arr[0])
