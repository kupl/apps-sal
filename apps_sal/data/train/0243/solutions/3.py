class Solution:

    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        doubles = set()
        for f, b in zip(fronts, backs):
            if f == b:
                doubles.add(f)

        min_x = None
        for f, b in zip(fronts, backs):
            if f not in doubles:
                if min_x:
                    min_x = min(min_x, f)
                else:
                    min_x = f

            if b not in doubles:
                if min_x:
                    min_x = min(min_x, b)
                else:
                    min_x = b

        if not min_x:
            return 0
        return min_x
