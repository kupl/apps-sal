class Solution:

    def knightDialer(self, n: int) -> int:
        adj_graph = {1: [8, 6], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [4, 2], 0: [4, 6]}

        def moveHelper(num, n, memo):
            if n == 1:
                return 1
            sumCounts = 0
            for number in adj_graph[num]:
                if (number, n - 1) in memo:
                    sumCounts += memo[number, n - 1]
                else:
                    res = moveHelper(number, n - 1, memo)
                    sumCounts += res
                    memo[number, n - 1] = res
            return sumCounts
        sumCount = 0
        memo = {}
        for k in list(adj_graph.keys()):
            sumCount += moveHelper(k, n, memo)
        return sumCount % (pow(10, 9) + 7)
