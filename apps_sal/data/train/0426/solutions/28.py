from typing import List


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        def trans(i) -> List[str]:
            res = []
            while i > 0:
                res.append(i % 10)
                i = i // 10
            return sorted(res)

        for i in range(31):
            if trans(N) == trans(1 << i):
                return True
        return False


