class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = {
            0: [4,6],
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [0,3,9],
            5: [],
            6: [0,1,7],
            7: [2,6],
            8: [1,3],
            9: [2,4]
        }
        def helper(pos, hops_left):
            if hops_left == 1: return 1
            if (pos, hops_left) in cache:
                return cache[(pos, hops_left)]
            else:
                sequences = 0
                for ne in neighbors[pos]:
                    sequences += helper(ne, hops_left-1)
                cache[(pos, hops_left)] = sequences
                # print(f\"seq {sequences} for (pos {pos}, hops_left {hops_left})\")
                return sequences
        cache = {}
        counts = [0]*10
        for start in range(10):
            counts[start] = helper(start, n)
            # print(f\"counts[{start}] = {counts[start]}\")
        return sum(counts)%(10**9+7)
