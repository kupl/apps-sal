class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        seen = {}
        A.sort()
        for (ind, i) in enumerate(A):
            if i / 2 in seen:
                seen[i / 2] -= 1
                if seen[i / 2] == 0:
                    del seen[i / 2]
            elif 2 * i in seen:
                seen[2 * i] -= 1
                if seen[2 * i] == 0:
                    del seen[2 * i]
            elif i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        print(seen)
        return not bool(seen)
