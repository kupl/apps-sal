class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        from collections import Counter
        dic = sorted(Counter(nums).items())
        res = [dic[0][0]]
        # print(dic)
        if dic[0][1] > 3:
            res += [dic[0][0]] * 3
        elif dic[0][1] == 3:
            res += [dic[0][0]] * 2
            res.append(dic[1][0])
        elif dic[0][1] == 2:
            res.append(dic[0][0])
            res.append(dic[1][0])
            if dic[1][1] > 1:
                res.append(dic[1][0])
            else:
                res.append(dic[2][0])
        else:
            res.append(dic[1][0])
            if dic[1][1] > 2:
                res.append(dic[1][0])
                res.append(dic[1][0])
            elif dic[1][1] == 2:
                res.append(dic[1][0])
                res.append(dic[2][0])
            else:
                res.append(dic[2][0])
                if dic[2][1] > 1:
                    res.append(dic[2][0])
                else:
                    res.append(dic[3][0])
        if dic[-1][1] > 3:
            res = [dic[-1][0] - res[i] for i in range(4)]
        elif dic[-1][1] == 3:
            res = [dic[-1][0] - res[i] for i in range(1, 4)] + [dic[-2][0] - res[0]]
        elif dic[-1][1] == 2:
            tmp = [dic[-1][0] - res[i] for i in range(2, 4)]
            if dic[-2][1] > 1:
                tmp += [dic[-2][0] - res[0]] + [dic[-2][0] - res[1]]
            else:
                tmp += [dic[-3][0] - res[0]] + [dic[-2][0] - res[1]]
            res = tmp
        else:
            tmp = [dic[-1][0] - res[3]]
            if dic[-2][1] > 2:
                tmp += [dic[-2][0] - res[i] for i in range(3)]
            elif dic[-2][1] == 2:
                tmp += [dic[-2][0] - res[i] for i in range(1, 3)]
                tmp += [dic[-3][0] - res[0]]
            else:
                tmp += [dic[-2][0] - res[2]]
                tmp += [dic[-3][0] - res[1]]
                if dic[-3][1] > 1:
                    tmp += [dic[-3][0] - res[0]]
                else:
                    tmp += [dic[-4][0] - res[0]]
            res = tmp
        return min(res)
