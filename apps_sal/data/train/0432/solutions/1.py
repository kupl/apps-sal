class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        q = collections.deque()
        counter = collections.Counter(sorted(nums))
        for item in counter.items():
            number = item[0]
            count = item[1]
            if count < len(q):
                return False
            elif count > len(q):
                for i in range(count - len(q)):
                    q.append(number + k - 1)
            while len(q) != 0 and q[0] == number:
                q.popleft()
        return len(q) == 0
