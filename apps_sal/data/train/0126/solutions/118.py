class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = defaultdict(int)
        for size in range(minSize, maxSize + 1):
            q = deque()
            for i in range(0, len(s)):
                q.append(s[i])
                if i > size - 1:
                    q.popleft()
                if i >= size - 1 and len(set(q)) <= maxLetters:
                    count[tuple(q)] += 1
        if len(count) == 0:
            return 0
        return max(count.values())
