class Solution:

    def equalSubstring(self, string: str, target: str, maxCost: int) -> int:
        cost = [0] * len(string)
        for i in range(len(string)):
            if string[i] != target[i]:
                cost[i] += abs(ord(string[i]) - ord(target[i]))
            if i > 0:
                cost[i] += cost[i - 1]
        answer = 0
        s = 0
        for i in range(len(string)):
            if cost[i] <= maxCost:
                answer = max(answer, i + 1)
            else:
                while s <= i and cost[i] - cost[s] > maxCost:
                    s += 1
                answer = max(answer, i - s)
        return answer
