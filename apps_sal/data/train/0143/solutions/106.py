class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        max_count = 0
        tree_len = len(tree)
        if len(tree) == 1:
            return 1
        if len(set(tree)) in (1,2):
            return len(tree)
        for i in range(tree_len - 1):
            tree_set = set()
            tree_set.add(tree[i])
            count = 1
            for j in range(i+1, tree_len):
                if tree[j] not in tree_set and len(tree_set) == 2:
                    break
                tree_set.add(tree[j])
                count += 1
            max_count = max(max_count, count)
        return max_count
                

