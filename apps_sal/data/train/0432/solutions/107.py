class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)
        que = collections.deque()
        last_required = 0
        last_num = 0
        for num, num_count in sorted(count.items()):
            if last_required > 0 and last_num + 1 != num or num_count < last_required:
                return False
            que.append(num_count - last_required)
            last_required = num_count
            if len(que) == k:
                last_required -= que.popleft()
            last_num = num
        return last_required == 0

    def isPossibleDivide_II(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)
        for next_num in sorted(count):
            next_dup = count[next_num]
            for j in range(next_num, next_num + k):
                if count[j] < next_dup:
                    return False
                count[j] -= next_dup
        return True
