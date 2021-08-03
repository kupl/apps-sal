import functools as ft
import typing as t


class Solution:

    BASE = 10 ** 9 + 7

    def divisor_pairs(self, idx: int) -> List[t.Tuple[int, int]]:
        num = self.A[idx]
        left_idx = 0
        ans = []
        while self.A[left_idx] ** 2 <= num:
            left = self.A[left_idx]
            if num % left == 0:
                right = num // left
                if right in self.A_idx:
                    ans.append((left_idx, self.A_idx[right]))
            left_idx += 1
        return ans

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        self.A = sorted(A)
        self.A_idx = {a: idx for idx, a in enumerate(self.A)}
        return sum(self.count_binary_trees(idx) for idx in range(len(A))) % self.BASE

    @ft.lru_cache(None)
    def count_binary_trees(self, idx: int) -> int:
        num = self.A[idx]
        ans = 1  # root only
        for left_idx, right_idx in self.divisor_pairs(idx):
            left_cnt = self.count_binary_trees(left_idx)
            right_cnt = self.count_binary_trees(right_idx)
            if left_idx == right_idx:
                total_cnt = left_cnt * right_cnt
            else:
                total_cnt = 2 * left_cnt * right_cnt
            ans += total_cnt
        return ans
