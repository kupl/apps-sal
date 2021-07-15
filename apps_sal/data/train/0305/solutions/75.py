class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        '''
        ccbccbcabc
        Input: text = \"abcabcabc\"
        Output: 3
        Explanation: The 3 substrings are \"abcabc\", \"bcabca\" and \"cabcab\".
        
        def EchoLen(i,j): length of echo string xxxi,xxxj
            if i<0: return 0
            if i == j: return 0
            if text[i] == text[j]:
                res = 1+EchoLen(i-1,-1j)
            else: 
                res = 0
        
        
        if text[i] == text[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else: dp[i][j] = 0
        
        
        '''
        res = set()
        dp = [[0 for _ in range(len(text))] for _ in range(len(text))]
        for i in range(len(text)):
            for j in range(i+1,len(text)):
                if i == 0:
                    if text[i] == text[j]:
                        dp[i][j] = 1
                else:
                    if text[i] == text[j]:
                        dp[i][j] = 1+dp[i-1][j-1]
        # print(dp)
        for i in range(len(text)):
            for j in range(i+1,len(text)):
                if (j-i+1)%2==0:
                    m = (i+j)//2
                    if dp[m][j]>=(j-m): 
                        # print(i,j,m)
                        res.add(text[i:m+1])
        print(res)
        return len(res)
                    

