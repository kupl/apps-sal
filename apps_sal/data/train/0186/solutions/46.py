class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:
        return self.helper(cost, target, {})

    def helper(self, cost, target, visited):
        if target == 0:
            return ''
        if target in visited:
            return visited[target]
        ans = '0'
        for i in range(1, 10):
            if target >= cost[i - 1]:
                prev = self.helper(cost, target - cost[i - 1], visited)
                if prev != '0':
                    curr = str(i) + prev
                    if len(curr) >= len(ans) and int(curr) > int(ans):
                        ans = curr
        visited[target] = ans
        return ans
