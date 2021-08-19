class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        currCost = 0
        maxLength = 0
        start = 0
        curr = 0
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        print(costs)
        while curr < len(costs):
            currCost += costs[curr]
            while currCost > maxCost:
                currCost = currCost - costs[start]
                start += 1
            if curr - start + 1 > maxLength:
                maxLength = curr - start + 1
            curr += 1
        return maxLength
