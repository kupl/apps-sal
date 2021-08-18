class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        c = Counter(nums)
        nums = list(set(nums))
        heapify(nums)
        print(nums)
        while nums:
            m = heappop(nums)
            while nums and c[m] == 0:
                m = heappop(nums)
            for i in range(1, k):
                if c[m + i] < c[m]:
                    print((c[m + i], c[m], m))
                    return False
                c[m + i] -= c[m]
            c[m] = 0
        return True
