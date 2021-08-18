from collections import Counter
from collections import deque


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        count = deque(sorted([(count[k], k) for k in count]))
        while count and k >= count[0][0]:
            k -= count.popleft()[0]
        return len(count)
