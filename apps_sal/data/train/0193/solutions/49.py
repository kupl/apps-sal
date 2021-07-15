class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        num = {}
        
        for i in arr:
            if i in num:
                num[i] += 1
            else:
                num[i] = 1
        
        sort_nums = sorted(num.items(), key=lambda x: x[1], reverse=True)
        
        total = 0
        ind = 0
        
        for i in sort_nums:
            if total < len(arr) / 2:
                total += i[1]
                ind += 1
            else:
                break
        
        return ind
