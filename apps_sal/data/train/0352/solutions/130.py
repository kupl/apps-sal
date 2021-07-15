class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_sort = [(len(word), word) for word in words]
        words_sort.sort()
        words = [word for w_len, word in words_sort]
        
        
        def isPredecessor(pre:str, succ:str) -> bool:
            
            if len(pre) != len(succ)-1:
                return False
            
            pre = pre + '.'
            d = 0
            for i in range(len(succ)):
                if pre[i-d] != succ[i]:
                    d += 1
                    if d>=2:
                        return False
            return True
        
        
        chain = [1] * len(words)
        ans = 1
        for i in range(len(words)):
            for j in range(0, i):
                if isPredecessor(words[j], words[i]):
                    chain[i] = max(chain[i], chain[j]+1)
                    ans = max(ans, chain[i])
        
        return ans
