class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        totalCost = 0
        maxLength = 0

        costs = []
        left = 0
        length = 0
        for i in range(len(s)):
            costs.append(abs(ord(s[i]) - ord(t[i])))
            totalCost += costs[-1]
            length += 1

            if totalCost <= maxCost:
                maxLength = length if length > maxLength else maxLength
            else:
                while totalCost > maxCost:
                    totalCost -= costs[left]
                    left += 1
                    length -= 1

        return maxLength
