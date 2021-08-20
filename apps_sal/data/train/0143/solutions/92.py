class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        if tree == [] or tree is None:
            return 0
        if len(tree) == 1:
            return 1
        s = 0
        max = 1
        count = max
        for i in range(len(tree)):
            j = i + 1
            b1 = tree[i]
            b2 = tree[j]
            count = 1
            if b1 == b2:
                while j < len(tree) and tree[j] == b1:
                    j += 1
                    count += 1
                if j != len(tree):
                    b2 = tree[j]
                elif count > max:
                    return count
            while j < len(tree):
                if tree[j] != b1 and tree[j] != b2:
                    if count >= max:
                        max = count
                    break
                count += 1
                j += 1
                if j == len(tree):
                    if count >= max:
                        max = count
                    return max
        return max
