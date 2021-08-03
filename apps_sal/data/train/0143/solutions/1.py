class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        best_so_far = start = 0
        fruit_1 = fruit_2 = fruit_1_last_index = fruit_2_last_index = None

        for end in range(len(tree)):
            if fruit_1 is None:
                fruit_1 = tree[end]
                fruit_1_last_index = end

            elif fruit_2 is None and tree[end] != fruit_1:
                fruit_2 = tree[end]
                fruit_2_last_index = end

            else:
                if tree[end] == fruit_1:
                    fruit_1_last_index = end
                elif tree[end] == fruit_2:
                    fruit_2_last_index = end
                else:
                    best_so_far = max(best_so_far, end - start)

                    if fruit_1_last_index < fruit_2_last_index:
                        start = fruit_1_last_index + 1
                        fruit_1 = tree[end]
                        fruit_1_last_index = end
                    else:
                        start = fruit_2_last_index + 1
                        fruit_2 = tree[end]
                        fruit_2_last_index = end

        return max(best_so_far, len(tree) - start)
