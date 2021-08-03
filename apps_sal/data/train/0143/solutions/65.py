class Solution:
    def totalFruit(self, tree: List[int]) -> int:

        res = 0

        mres = 0
        temp = set()
        i = 0
        newidx = 0

        while i < len(tree):
            if len(temp) == 0:
                mres += 1
                temp.add(tree[i])
                i += 1

            elif len(temp) == 1:
                newidx = i
                temp.add(tree[i])
                mres += 1
                i += 1

            else:
                if tree[i] in temp:
                    mres += 1
                    i += 1
                else:
                    res = max(res, mres)
                    mres = 0
                    temp = set()
                    i = newidx

        res = max(res, mres)
        return res
