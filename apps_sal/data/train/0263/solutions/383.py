class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                 [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        sol = []
        cache = {}

        def backtrack(pos, hops, cur):
            if (pos, hops) in cache:
                return cache[(pos, hops)]
            if hops == 0:
                return 1
            count = 0
            for nbr in moves[pos]:
                cur.append(nbr)
                count += backtrack(nbr, hops - 1, cur)
                cur.pop()
            cache[(pos, hops)] = count
            return count

        counts = 0
        for pos in range(10):
            counts += backtrack(pos, n - 1, [])

        return counts % (10**9 + 7)

#         cur_hops = 1
#         prev_counts = [1]*10
#         cur_counts = [0]*10

#         while cur_hops < n:
#             cur_hops += 1
#             cur_counts = [0]*10

#             for pos in range(10):
#                 for nbr in moves[pos]:
#                     cur_counts[pos] += prev_counts[nbr]
#             prev_counts = cur_counts

#         return sum(prev_counts)%(10**9+7)
