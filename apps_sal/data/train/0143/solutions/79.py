class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) == 1:
            return 1

        window_start = 0
        window_end = 2
        total_max = 2

        if tree[0] == tree[1]:
            tmp_index = 0
        else:
            tmp_index = 1

        fruit_type = set(tree[:2])

        for i in range(2, len(tree)):
            if (tree[i] in fruit_type) or len(fruit_type) < 2:
                window_end += 1
                if tree[i] != tree[i - 1]:
                    tmp_index = i
                fruit_type.add(tree[i])
            else:
                window_start = tmp_index
                tmp_index = i
                window_end += 1
                fruit_type = set(tree[i - 1:i + 1])
            #print(window_start, window_end, fruit_type)
            if window_end - window_start > total_max:
                total_max = window_end - window_start
        return total_max
