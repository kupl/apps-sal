class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) <= 2:
            return len(tree)
        collection_list = [tree[0]]
        counter = 1
        _max = 1
        rep = 1
        for i in range(1, len(tree)):
            if tree[i] in collection_list:
                if tree[i] == tree[i - 1]:
                    rep += 1
                else:
                    rep = 1
                counter += 1
                if counter > _max:
                    _max = counter
            elif len(collection_list) == 1:
                collection_list.append(tree[i])
                counter += 1
                rep = 1
                if counter > _max:
                    _max = counter
            else:
                collection_list = [tree[i - 1], tree[i]]
                counter = 1 + rep
                rep = 1
        return _max
