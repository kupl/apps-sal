class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        blocks = []

        i = 0
        while i < len(tree):
            j = i + 1
            length = 1
            while j < len(tree) and tree[j] == tree[j - 1]:
                length += 1
                j += 1

            blocks.append((tree[i], length))
            i = j

        maxi = 0

        i = 0
        while i < len(blocks):
            types, cur = set(), 0
            for j in range(i, len(blocks)):
                types.add(blocks[j][0])
                cur += blocks[j][1]
                if len(types) > 2:
                    i = j - 1
                    break

                maxi = max(maxi, cur)
            else:
                break
        return maxi
