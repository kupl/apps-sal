class Solution:

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        memory = []
        for i in range(len(triangle)):
            memory.append({})
        return self.helper(memory, triangle, 0, 0)

    def helper(self, memory, triangle, i, j):
        if i >= len(triangle):
            return 0
        if memory[i].get(j) is None:
            memory[i][j] = triangle[i][j] + min(self.helper(memory, triangle, i + 1, j), self.helper(memory, triangle, i + 1, j + 1))
        return memory[i][j]
