class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        s=0
        res=0
        for a in satisfaction:
            s+=a
            if s<=0:
                break
            res+=s
        return res
    
    
    
    
    '''
    将所有大于的的前缀子串都加上
    大数尽可能多家几次，所以先倒序
    到当前位置的前缀和
    一直计算前缀和，直到前缀和<=0  结束
    [9, 8, 5, 2, 1, -1]
sum = 9 * 4 + 8 * 3 + 2 * 3 + 1 * 2 + -1 * 1
<=>
sum += 9
sum += (9 + 8 = 17)
sum += (17 + 2 = 19)
sum += (19 + 1 = 20)
sum += (20 – 1 = 19)
    '''
