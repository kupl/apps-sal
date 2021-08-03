class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        count = collections.Counter()
        i = ans = 0

        for j in range(len(tree)):
            fruit = tree[j]
            count[fruit] += 1

            while len(count.keys()) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1

            ans = max(ans, j - i + 1)

        return ans
