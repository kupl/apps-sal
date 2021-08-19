class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # establish the first sum
        s = 0
        ret = 0
        for i, num in enumerate(arr):
            if i - k < 0:
                s += num
                if s >= threshold * k and i == k - 1:
                    ret += 1
                    print(i)
                continue
            s -= arr[i - k]
            s += num
            if s >= threshold * k:
                ret += 1
                print(i)
        return ret
