class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        cnt = Counter(nums)
        no = min(cnt.keys())
        while cnt:
            for j in range(k):
                if cnt[no] == 0:
                    return False
                cnt[no] -= 1
                if cnt[no] == 0:
                    cnt.pop(no)
                no += 1
            if cnt:
                no = min(cnt.keys())
        return True
