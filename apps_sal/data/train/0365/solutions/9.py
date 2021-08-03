class Solution:
    def uniqueLetterString(self, s: str) -> int:

        ind = collections.defaultdict(list)
        for i, v in enumerate(s):
            ind[v].append(i)

        ans, n = 0, len(s)
        for i, v in ind.items():
            temp = 0
            # print(i,v, temp)
            for k, index in enumerate(v):
                if k == 0 and k == len(v) - 1:
                    temp += (index + 1) * (n - index)
                elif k == 0:
                    temp += (index + 1) * (v[k + 1] - index)
                elif k > 0 and k < len(v) - 1:
                    temp += (index - v[k - 1]) * (v[k + 1] - index)
                elif k == len(v) - 1:
                    temp += (index - v[k - 1]) * (n - index)
                # print(k,index,temp)
            ans += temp
            # print('-----------------------')

        return ans
