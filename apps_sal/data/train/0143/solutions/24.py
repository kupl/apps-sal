class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        i = 0
        j = 0
        hm = {}
        maxL = 0
        while j < len(tree):
            if tree[j] in hm:
                hm[tree[j]] += 1
            else:
                if len(hm) < 2:
                    hm[tree[j]] = 1
                else:
                    maxL = max(maxL, j - i)
                    while i < j and len(hm) > 1:
                        hm[tree[i]] -= 1
                        if hm[tree[i]] == 0:
                            del hm[tree[i]]
                        i += 1
                    hm[tree[j]] = 1

            j += 1

        maxL = max(maxL, j - i)
        return maxL
