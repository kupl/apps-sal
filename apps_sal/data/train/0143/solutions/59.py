class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        start = 0
        end = 1
        maxLength = 1
        types = {}
        types[tree[0]] = 1

        if len(tree) <= 2:
            return len(tree)

        while end < len(tree) - 1 or start < end:
            if end < len(tree) - 1 and len(types) < 2:
                if types.get(tree[end]):
                    types[tree[end]] += 1
                else:
                    types[tree[end]] = 1

                end += 1
            elif end == len(tree) or types.get(tree[end]) == None:
                types[tree[start]] -= 1

                if types[tree[start]] == 0:
                    del types[tree[start]]

                start += 1
            else:
                if types.get(tree[end]):
                    types[tree[end]] += 1
                else:
                    types[tree[end]] = 1

                end += 1

            if len(types) <= 2:
                maxLength = max(maxLength, end - start)

        return maxLength
