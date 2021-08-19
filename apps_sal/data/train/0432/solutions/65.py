class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        D = deque()
        if len(nums) % k != 0:
            return False
        target_set_count = len(nums) // k
        for num in nums:
            if len(D):
                (prev_val, count) = D.pop()
                if num == prev_val + 1:
                    prev_val += 1
                    count += 1
                else:
                    D.appendleft((prev_val, count))
                    count = 1
            else:
                (prev_val, count) = (num, 1)
            if count < k:
                D.appendleft((prev_val, count))
            if len(D) > target_set_count:
                break
        return len(D) == 0
