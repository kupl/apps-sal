class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        ans = 0
        p = 0
        while p < len(tree):
            acc = 1
            first = tree[p]
            next_p = len(tree)
            second = -1
            for i in range(p + 1, len(tree)):
                if tree[i] != first:
                    if second == -1:
                        second = tree[i]
                        next_p = i
                    elif tree[i] != second:
                        break
                acc += 1
                if i == len(tree) - 1:
                    return max(ans, acc)
            p = next_p
            ans = max(ans, acc)
        return ans
