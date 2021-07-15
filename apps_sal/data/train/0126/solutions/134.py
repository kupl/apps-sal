class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
       
        start = 0
        end = 0
        sub = {}
        result = {}
        self.max_size = 0
        
        def add_sub(pos):
            if s[pos] in sub:
                sub[s[pos]] +=1
            else:
                sub[s[pos]] = 1
        
        def rem_sub(pos):
            if s[pos] in sub:
                if sub[s[pos]] == 1:
                    del sub[s[pos]]
                else:
                    sub[s[pos]] -= 1
        def add_res(string):
            if string in result:
                result[string] +=1
            else:
                result[string] = 1
            self.max_size = max(self.max_size,result[string])
        
        for size in range(minSize,maxSize+1):
            while start <= len(s)-size:
                if (end-start)+1 < size:
                    add_sub(end)
                    end +=1
                else:
                    add_sub(end)
                    if len(sub) <= maxLetters:
                        add_res(s[start:end+1])
                    rem_sub(start)
                    start +=1
                    end +=1
            start = 0
            end = 0
            sub = {}
            
        return self.max_size
        
        
        

