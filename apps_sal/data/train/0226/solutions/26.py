from typing import List
from collections import defaultdict


class Solution:
    def helper(self, last_num, used, partners, index):
        if index == len(used):
            return 1
        total = 0
        # print(partners, partners[last_num])
        for partner, partner_list in partners[last_num].items():
            for partner_index in partner_list:
                if not used[partner_index]:
                    used[partner_index] = True
                    total += self.helper(partner, used, partners, index + 1)
                    used[partner_index] = False
                    break
        return total

    def numSquarefulPerms(self, A: List[int]) -> int:
        squares = set()
        i = 0
        partners = defaultdict(lambda: defaultdict(set))
        while i * i <= 200000000:
            squares.add(i * i)
            i += 1
        for i in range(len(A)):
            for j in range(i + 1, len(A), 1):
                if A[i] + A[j] in squares:
                    partners[A[i]][A[j]].add(j)
                    partners[A[j]][A[i]].add(i)
        unique_nums = dict()
        for i, num in enumerate(A):
            unique_nums[num] = i
        used = [False for _ in A]
        total = 0
        for num, i in unique_nums.items():
            used[i] = True
            total += self.helper(num, used, partners, 1)
            used[i] = False
        return total
