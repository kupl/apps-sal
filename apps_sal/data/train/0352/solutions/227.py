class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        #backtrack/ bfs/dfs?
        # back -> longest to smallest?
        
        words.sort(key = lambda x:len(x))
        print(words)
        n_s=len(words[0])
        
        dic = collections.defaultdict(lambda:0)
        longest_chain = 1
        
        def search(word):
            if len(word)==n_s:
                dic[word] = 1
                return 1
            N = 1
            for i in range(0,len(word)):
                sub = word[0:i] + word[i+1:]
                
                if sub in words:
                    n = search(sub)
                    
                    N =max(N,n+1)
            dic[word]=N
            nonlocal longest_chain
            longest_chain = max(longest_chain,N)
            #print(N,longest_chain,word)
            return N
        
        for i in range(len(words)-1,-1,-1):
            if dic[words[i]] in dic:
                continue
            word = words[i]
            re = search(word)
            longest_chain = max (longest_chain,re)
        return longest_chain

