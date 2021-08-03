class Solution:
    def knightDialer(self, n: int) -> int:

        dialer_map = {0: [4, 6],
                      1: [6, 8],
                      2: [7, 9],
                      3: [4, 8],
                      4: [0, 3, 9],
                      5: [],
                      6: [0, 1, 7],
                      7: [2, 6],
                      8: [1, 3],
                      9: [2, 4]}

        total = 0
        for i in range(10):
            if i == 5 and n == 1:
                total += 1
                continue

            level = {i: 1}
            curr = 1
            while curr < n:
                next_level = defaultdict(lambda: 0)
                for l in list(level.keys()):
                    for d in dialer_map[l]:
                        next_level[d] += level[l]

                level = next_level
                curr += 1
            count = sum(level.values())
            total += count

        return total % (10**9 + 7)
