class Solution:
    def totalFruit(self, tree: List[int]) -> int:

        # compress the tree
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
            # We'll start our scan at block[i].
            # types : the different values of tree[i] seen
            # weight : the total number of trees represented
            #          by blocks under consideration
            types, weight = set(), 0

            # For each block from i and going forward,
            for j in range(i, len(compressedTree)):
                # Add each block to consideration
                types.add(compressedTree[j][0])
                weight += compressedTree[j][1]

                # If we have 3 types, this is not a legal subarray
                if len(types) >= 3:
                    i = j - 1
                    break

                ans = max(ans, weight)

            # If we go to the last block, then stop
            else:
                break

        return ans
