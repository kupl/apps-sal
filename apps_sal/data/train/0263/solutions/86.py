
class Solution:
    def knightDialer(self, n: int) -> int:
        d = {0: (4, 6),
             1: (6, 8),
             2: (7, 9),
             3: (4, 8),
             4: (0, 3, 9),
             5: (),
             6: (0, 1, 7),
             7: (2, 6),
             8: (1, 3),
             9: (2, 4)}

        prev_level = {i: 1 for i in range(10)}
        for j in range(1, n):
            curr_level = defaultdict(int)
            for i, freq in list(prev_level.items()):
                for child in d[i]:
                    curr_level[child] += freq
            prev_level = curr_level

        return sum(prev_level.values()) % (10**9 + 7)
