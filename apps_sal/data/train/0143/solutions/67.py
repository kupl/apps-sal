class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        item1_val = -1
        item1_fs = -1
        item1_ls = -1
        item2_val = -1
        item2_fs = -1
        item2_ls = -1
        size = list()
        for i in range(len(tree)):
            if tree[i] == item1_val:
                item1_ls = i
                if item1_fs == -1:
                    item1_ls = i
                if i == 0:
                    size.append(1)
                size.append(size[i - 1] + 1)
            elif tree[i] == item2_val:
                item2_ls = i
                if item2_fs == -1:
                    item2_ls = i
                if i == 0:
                    size.append(1)
                size.append(size[i - 1] + 1)
            else:
                if item1_ls > item2_ls:  # item1 stays
                    item1_fs = item2_ls + 1
                    item2_val = tree[i]
                    item2_fs = i
                    item2_ls = i
                    size.append(i - item1_fs + 1)
                else:  # item2 stays
                    item2_fs = item1_ls + 1
                    item1_val = tree[i]
                    item1_fs = i
                    item1_ls = i
                    size.append(i - item2_fs + 1)

        return(max(size))
