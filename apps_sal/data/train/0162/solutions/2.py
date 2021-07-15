class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        s1,s2=text1,text2
        len_s1,len_s2=len(s1),len(s2)
        pick_s1_or_s2,pick_s1,pick_s2=0,1,2
        
        
        match_table=[[0 for i in range(len_s2)] for j in range(len_s1)]
        
        for i in range(len_s1):
            for j in range(len_s2):
                
                if(s1[i]==s2[j]):
                    
                    if(i==0 or j==0):
                        match_table[i][j]=1
                    
                    else:
                        match_table[i][j]=1+match_table[i-1][j-1]
                else:
                    if(i==0 and j>0):
                        match_table[i][j]=match_table[i][j-1]
                    elif(j==0 and i>0):
                        match_table[i][j]=match_table[i-1][j]
                    elif(i>0 and j>0):
                        if(match_table[i-1][j]>match_table[i][j-1]):
                            match_table[i][j]=match_table[i-1][j]
                        else:
                            match_table[i][j]=match_table[i][j-1]
        return match_table[len_s1-1][len_s2-1]
                        
        
        
                                      
        

