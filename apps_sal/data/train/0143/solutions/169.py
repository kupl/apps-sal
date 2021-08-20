class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        compressedTree = []
        current = [tree[0], 0]
        for index in range(len(tree)):
            fruit = tree[index]
            if fruit != current[0]:
                compressedTree.append(current)
                current = [fruit, 1]
            else:
                current[1] += 1
        compressedTree.append(current)
        ans = i = 0
        while i < len(compressedTree):
            (types, weight) = (set(), 0)
            for j in range(i, len(compressedTree)):
                types.add(compressedTree[j][0])
                weight += compressedTree[j][1]
                if len(types) >= 3:
                    i = j - 1
                    break
                ans = max(ans, weight)
            else:
                break
        return ans
