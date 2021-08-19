class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        result = 0
        ptr = 0
        count = collections.Counter()
        for (i, t) in enumerate(tree):
            count[t] += 1
            while len(count) >= 3:
                count[tree[ptr]] -= 1
                if count[tree[ptr]] == 0:
                    del count[tree[ptr]]
                ptr += 1
            result = max(result, i - ptr + 1)
        return result
