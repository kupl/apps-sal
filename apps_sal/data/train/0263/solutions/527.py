class Solution:
    def knightDialer(self, N: int) -> int:
        D = 10**9 + 7
        l = [1 for _ in range(10)]
        for _ in range(N - 1):
            l = self.transform_list(l)
            l = [x % D for x in l]
        return sum(l) % D

    def transform_list(self, l: List[int]) -> List[int]:
        # 0 -> 4, 6
        # 1 -> 6, 8
        # 2 -> 7, 9
        # 3 -> 4, 8
        # 4 -> 3, 9, 0
        # 5 -> None
        # 6 -> 1, 7, 0
        # 7 -> 2, 6
        # 8 -> 1, 3
        # 9 -> 2, 4
        nl = [0 for _ in range(10)]
        nl[0] = l[4] + l[6]
        nl[1] = l[6] + l[8]
        nl[2] = l[7] + l[9]
        nl[3] = l[4] + l[8]
        nl[4] = l[3] + l[9] + l[0]
        nl[6] = l[1] + l[7] + l[0]
        nl[7] = l[2] + l[6]
        nl[8] = l[1] + l[3]
        nl[9] = l[2] + l[4]
        return nl
