class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        dic = {}
        for i,j in zip(values,labels):
            if j not in dic:
                dic[j] = [i]
            else:
                dic[j].append(i)
        
        res_arr = []
        
        for i in dic:
            res_arr.extend(sorted(dic[i],reverse=True)[0:use_limit])
        
        res_arr.sort()
        count = 0
        res = 0
        while count < num_wanted and len(res_arr) > 0:
            tmp  = res_arr.pop()
            res += tmp
            count += 1
        return res
        

