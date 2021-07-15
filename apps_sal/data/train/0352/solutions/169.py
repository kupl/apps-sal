class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def chain(w1, w2):                         # check if w1 is a chain to w2
            m, n = len(w1), len(w2)
            if abs(m-n) != 1: return False
            i, j, one = 0, 0, 1
            while i < m and j < n:
                if w1[i] == w2[j]: i, j = i+1, j+1
                elif one: one, i = 0, i+1
                else: return False    
            return True
                    
        if not words: return 0
        words.sort(key=lambda x: len(x))
        n = len(words)
        dp = [1] * n
        ans = 1
        for i in range(n):
            for j in range(i): # visited all previous words[j] to check if dp[i] can reach a longer chain
                if chain(words[i], words[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        return ans        
#https://blog.csdn.net/JamieLuo/article/details/106486186?utm_medium=distribute.pc_relevant.none-task-blog-searchFromBaidu-2.add_param_isCf&depth_1-utm_source=distribute.pc_relevant.none-task-blog-searchFromBaidu-2.add_param_isCf
#先把所有的words按照长度进行sort
#dp[i]：包含第i个单词在内的最长链
#dp[i] = max(dp[j]) + 1，其中j<i且words[j]是words[i]的前缀
#另外，在判断是否是前缀时：（1)pre一定是word的长度-1；（2)遍历两者，两者应该只有一个字母不同

