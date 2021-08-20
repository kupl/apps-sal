class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        blocks = []
        i = 0
        while i < len(tree):
            start = i
            while i + 1 < len(tree) and tree[i + 1] == tree[start]:
                i += 1
            blocks.append((tree[start], i - start + 1))
            i = i + 1
        ans = 0
        i = 0
        while i < len(blocks):
            types = set()
            weight = 0
            j = i
            while j < len(blocks):
                types.add(blocks[j][0])
                weight += blocks[j][1]
                if len(types) > 2:
                    i = j - 1
                    break
                ans = max(ans, weight)
                j += 1
                if j == len(blocks):
                    i = j
            if i == len(blocks):
                break
        return ans
