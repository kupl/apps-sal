class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        
        # not the rolling hash method
        # optimize
        resultset = set()
        
        for i in range(len(text)):
            for j in range(i+1, len(text)):
                
                if text[i] == text[j]:
                    #compare two sliced string
                    str1 = text[i:j]
                    str2 = text[j: j+(j-i)]
                                       
                    if str1 == str2:
                        resultset.add(text[i: j+(j-i)])

        return len(resultset)

