class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        def minIndexGap(A, B) -> int:
            i = j = 0
            res = float('inf')
            while i < len(A) and j < len(B):
                if A[i] < B[j]:
                    res = min(res, B[j] - A[i] - 1)
                    i += 1
                else:
                    while j < len(B) and A[i] >= B[j]:
                        j += 1
            return res

        left = collections.defaultdict(list)
        right = collections.defaultdict(list)

        s = sum(nums)
        if s % p == 0:
            return 0
        elif s < p:
            return -1
        else:
            target = s % p

        key = 0
        for i, n in enumerate(nums):
            if n % p == target:
                return 1
            key = (n + key) % p
            left[key].append(i)

        key = 0
        for i, n in reversed(list(enumerate(nums))):
            key = (n + key) % p
            right[key].append(i)

        res = float('inf')
        if target in left:
            res = min(res, min(left[target]) + 1)
        if target in right:
            res = min(res, len(nums) - max(right[target]))

        for key in left:
            if p - key in right:
                res = min(res, minIndexGap(sorted(left[key]), sorted(right[p - key])))

        if res == len(nums):
            return -1

        return res
