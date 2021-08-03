
class Solution:
    def totalFruit(self, tree) -> int:
        '''

        :param tree: : List[int]
        :return:
        '''
        n = len(tree)
        if n <= 2:
            return n
        tem = collections.Counter()
        res = 0
        i = 0
        j = 1
        tem.update(tree[:1])

        while j < n:
            while j < n and len(tem.keys()) <= 2:
                tem.update([tree[j]])
                res = max(res, j - i)
                j += 1

            while len(tem.keys()) >= 3:
                tem[tree[i]] -= 1
                if tem[tree[i]] == 0:
                    tem.pop(tree[i])
                i += 1

            if j == n:
                res = max(res, j - i)
                break
        return res
