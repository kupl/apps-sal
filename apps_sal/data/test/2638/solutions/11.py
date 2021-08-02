class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        layer_costs = triangle[-1]

        for layer in range(len(triangle) - 2, -1, -1):  # range(start, end +- 1, step)
            for pos in range(len(triangle[layer])):
                min_cost = min(layer_costs[pos], layer_costs[pos + 1]) + triangle[layer][pos]
                layer_costs[pos] = min_cost

        return(layer_costs[0])
