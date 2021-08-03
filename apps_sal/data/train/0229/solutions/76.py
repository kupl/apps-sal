class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort()
        seen = Counter()
        for num in A:
            if num > 0 and num % 2:
                seen[num] += 1
                continue
            elem = 2 * num if num < 0 else num // 2
            if seen[elem] > 0:
                seen[elem] -= 1
            else:
                seen[num] += 1

        if sum(seen.values()):
            return False
        return True
