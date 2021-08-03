class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dp = [0.0 for _ in range(start)] + [1.0] + [0.0 for _ in range(start + 1, n)]
        dic = defaultdict(list)
        for e, p in zip(edges, succProb):
            dic[e[0]].append((e[1], p))
            dic[e[1]].append((e[0], p))

        queue = deque([start])
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                for c, p in dic[cur]:
                    if dp[cur] * p > dp[c]:
                        dp[c] = dp[cur] * p
                        queue.append(c)
        return dp[end]
