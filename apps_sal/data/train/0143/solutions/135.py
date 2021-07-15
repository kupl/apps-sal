class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # 包含两个元素的（因为题目说是两个篮子）的最长子序列，采苹果不能后退也不能跳过，所以就是连续子串,采的苹果个数就指的是子串长度
        # 跟之前的题目一模一样
        
        k = 2
        n = len(tree)
        if n < k:
            return n
        
        i = 0
        lookup = {}
        ans = 0
        # 1）有时候会晕是找到字典中的最小下标，还是找到字典中的重复下标
        # 2）因为这里并不是因为出现重复的key而需要移动左指针，而是因为字典里元素太多了而要移动左指针
        # 3）要找到重复了的key，那么就需要在插入之前去判断, 遇到重复的键值i = max(i, 1+lookUp[nums[j]])
        # 4）字典长度超标，不怕重复，因为重复的录入同一个键值一直记录的该key最后一次出现的位置，
        #    4.1）i_min = min(lookup.values()), 另 i= i_min+1, 之所以要一个中间变量i_min，是因为后面要用它去删除键值
        #    4.2）同时删除这个key，否则你每次取min都会找到这个数懂吗
        for j in range(n):
            lookup[tree[j]] = j
            if len(lookup) <= k:
                ans = max(ans, j-i+1)
            else:
                i_min = min(lookup.values())
                del lookup[tree[i_min]]
                i = i_min + 1
                
        return ans
                
            
            

