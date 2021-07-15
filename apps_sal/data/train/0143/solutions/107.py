class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        blocks = [(k, len(list(v)))
                  for k, v in itertools.groupby(tree)]

        ans = i = 0
        while i < len(blocks):
            # We'll start our scan at block[i].
            # types : the different values of tree[i] seen
            # weight : the total number of trees represented
            #          by blocks under consideration
            types, weight = set(), 0

            # For each block from i and going forward,
            for j in range(i, len(blocks)):
                # Add each block to consideration
                types.add(blocks[j][0])
                weight += blocks[j][1]

                # If we have 3 types, this is not a legal subarray
                if len(types) >= 3:
                    i = j-1
                    break

                ans = max(ans, weight)

            # If we go to the last block, then stop
            else:
                break

        return ans
