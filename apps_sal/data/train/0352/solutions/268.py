class Solution:
    
    def longestStrChain(self, words: List[str]) -> int:
        x=lambda a:len(a)
        words.sort(key=x)
        print(words)
        chain_len=[None]*len(words)
        chain_len[0]=1
        
        
        
        
        for i in range(1,len(words)):
            temp=words[i]
            chain_len[i]=1
            for j in range(len(temp)):
                temp2=temp[:j]+temp[j+1:]
                if (temp2 not in words) :
                    continue
                for k in range(i-1,-1,-1):
                    if (len(words[k])<len(words[i])-1):
                        break        
                    else:
                          if (len(words[k])==len(words[i])-1):
                                  if words[k]==temp2:
                                        chain_len[i]=max(chain_len[i],chain_len[k]+1)
                                        break
                        
        return max(chain_len)
