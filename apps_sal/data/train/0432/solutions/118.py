class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        q = collections.deque()
        opened, prev = 0, -1
        cnt = collections.Counter(nums)
        for ele in sorted(cnt):
            if cnt[ele] < opened or opened > 0 and ele > prev + 1:
                return False
            q.append(cnt[ele] - opened)
            prev = ele
            opened = cnt[ele]
            if len(q) == k:
                opened -= q.popleft()
        return opened == 0
