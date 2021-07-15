class Solution:
    def knightDialer(self, n: int) -> int:
        nei = {
            1: [6, 8],
            2: [7, 9],
            3: [8, 4],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        def helper(n, curr, seen, nei):
            if n == 1:
                return 1
            if curr not in nei:
                return 0
            key = (n, curr)
            if key in seen:
                return seen[key]
            answer = 0
            for ne in nei[curr]:
                answer = (answer + helper(n - 1, ne, seen, nei)) % (10 ** 9 + 7)
            seen[key] = answer
            return answer
        total = 0
        seen = {}
        for i in range(10):
            total = (total + helper(n, i, seen, nei)) % (10 ** 9 + 7)
        return total

