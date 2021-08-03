class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        run_sum = 0
        count = 0
        book_keep = {0: 1}
        for num in nums:
            run_sum += num
            prev_sum = run_sum - target
            if prev_sum in book_keep:
                count += 1
                run_sum = 0
                book_keep.clear()
                book_keep = {0: 1}
            else:
                book_keep[run_sum] = 1

        return count
