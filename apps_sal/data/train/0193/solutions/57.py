class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        tmp_dict = {}
        for e in arr:
            if e not in tmp_dict:
                tmp_dict[e] = 1
            else:
                tmp_dict[e] += 1
        tmp = [(key, tmp_dict[key]) for key in tmp_dict]
        tmp.sort(key=lambda x: x[1], reverse=True)
        res = []
        cur = 0
        i = 0
        while cur < len(arr) // 2:
            res.append(tmp[i][0])
            cur += tmp[i][1]
            i += 1
        return len(res)
