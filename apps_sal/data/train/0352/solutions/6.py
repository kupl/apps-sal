class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def precedent(w1_c,w2_c):
            if len(w1_c)>len(w2_c):
                return False
            
            count = 0
            for c in w2_c:
                if c in w1_c:
                    count+= w2_c[c]-w1_c[c]
                else:
                    count+= w2_c[c]
            return count==1
                    
        minL = float('inf')
        maxL = float('-inf')
        
        longest = 1
        
        len_count = collections.defaultdict(list)
        subsequent_of_word = collections.defaultdict(int)
        count_of_word = collections.defaultdict(Counter)
        
        for w in words:
            len_count[len(w)].append(w)
            subsequent_of_word[w] = 1
            count_of_word[w] = Counter(w)
            maxL= max(maxL,len(w))
            minL= min(minL,len(w))

        for i in range(maxL-1,minL-1,-1):
            if i in len_count:
                if i+1 in len_count:
                    for w1 in len_count[i]:
                        for w2 in len_count[i+1]:
                            if precedent(count_of_word[w1],count_of_word[w2]):
                                subsequent_of_word[w1] = max(subsequent_of_word[w1], subsequent_of_word[w2]+1)
                                longest = max(longest, subsequent_of_word[w1])
                                
                else:
                    for w in len_count[i]:
                        subsequent_of_word[w]=1
        
        return longest
                        
        
                    
            
        
        
            
        
        

