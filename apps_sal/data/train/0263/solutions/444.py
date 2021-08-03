class Solution:
    def knightDialer(self, N: int) -> int:
        if N == 0:
            return 0

        dialer = [[1, 1, 1] for _ in range(4)]
        directions = [[-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2]]
        forbidden = set()
        forbidden.add((3, 0))
        forbidden.add((3, 2))
        for _ in range(1, N):
            tmp = [[0, 0, 0] for _ in range(4)]
            for i in range(4):
                for j in range(3):
                    if (i, j) not in forbidden:
                        for direction in directions:
                            new_i, new_j = i + direction[0], j + direction[1]
                            if 0 <= new_i < 4 and 0 <= new_j < 3:
                                tmp[new_i][new_j] += dialer[i][j]
            dialer = tmp

        return (sum(sum(dialer, [])) - dialer[3][0] - dialer[3][2]) % (10 ** 9 + 7)
