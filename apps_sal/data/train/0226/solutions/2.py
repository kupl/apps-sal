class Solution:

    def numSquarefulPerms(self, A: List[int]) -> int:

        def get_valid():
            ans = 0
            seen = set()
            visited = set()
            while q:
                (cur, remaining) = q.popleft()
                if not remaining and cur not in seen:
                    ans += 1
                for (i, n) in enumerate(remaining):
                    sq = (cur[-1] + n) ** 0.5
                    if float(int(sq)) == sq:
                        add = cur + (n,)
                        remain = remaining[:i] + remaining[i + 1:]
                        if (add, remain) not in visited:
                            q.append((add, remain))
                            visited.add((add, remain))
            return ans
        q = deque()
        for (i, num) in enumerate(A):
            q.append(((num,), tuple(A[:i] + A[i + 1:])))
        return get_valid()
