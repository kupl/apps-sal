class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        dic = {}
        first = 0
        i = 0
        n = len(tree)
        ans = 0
        while i < n:
            val = tree[i]
            if val in dic:
                dic[val] += 1
            elif len(dic) < 2:
                dic[val] = 1
            else:
                dic[val] = 1
                while len(dic) >= 2:
                    v2 = tree[first]
                    first += 1
                    dic[v2] -= 1
                    if dic[v2] == 0:
                        dic.pop(v2, None)
                        break
            ans = max(i - first + 1, ans)
            i += 1
        return ans
