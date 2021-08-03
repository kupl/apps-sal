class Solution:
    def totalFruit(self, tree: List[int]) -> int:

        st = c = res = 0
        dic = dict()
        for end in range(len(tree)):
            if tree[end] in dic:
                dic[tree[end]] += 1
            else:
                dic[tree[end]] = 1
                c += 1
            while c > 2:
                dic[tree[st]] -= 1
                if dic[tree[st]] == 0:
                    del dic[tree[st]]
                    c -= 1
                st += 1
            res = max(res, end - st + 1)
        return res
