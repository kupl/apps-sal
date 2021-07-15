class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic = {}
        n_arr = []
        res = 0
        length = len(arr)
        for i in arr:
            if i in list(dic.keys()):
                dic[i] += 1
            else:
                dic[i] = 1
        
        for i in dic:
            n_arr.append([dic[i], i])
        
        n_arr = sorted(n_arr)
        for i in range (len(n_arr) -1, -1, -1):
            length -= n_arr[i][0]
            res+=1
            if length <= len(arr)//2:
                break
        return res

