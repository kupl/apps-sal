class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        words.append(result)
        assigned = {}
        assigned_inv = [None] * 10
        self.r,self.c=len(words),max(list(map(len, words)))
        
        def dfs(column,row,bal):
            if column>=self.c:
                return bal==0 and all(assigned[i[0]]!=0 for i in words)
            if row==self.r:
                return bal%10==0 and dfs(column+1,0,bal//10)
            
            word=words[row]
            if column>=len(word):
                return dfs(column,row+1,bal)
            letter=word[~column]
            sign= 1 if row<self.r-1 else -1
            if letter in assigned:
                return dfs(column,row+1,bal+sign*assigned[letter])
            else:
                for num,c in enumerate(assigned_inv):
                    if c is None and (num or column!=len(word)-1):
                        assigned[letter]=num
                        assigned_inv[num]=letter
                        if dfs(column,row+1,bal+sign*num):
                            return True
                        assigned_inv[num]=None
                        del assigned[letter]
            return False
            
        return dfs(0,0,0)
                        
            
        
        
        

