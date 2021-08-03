class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        answer = 0
        start = 0

        for i in range(1, len(s)):
            if s[start] != s[i]:
                deletions = sorted(cost[start: i], reverse=True)

                while len(deletions) > 1:
                    answer += deletions.pop()

                start = i

        deletions = sorted(cost[start: len(s)], reverse=True)

        while len(deletions) > 1:
            answer += deletions.pop()

        return answer
