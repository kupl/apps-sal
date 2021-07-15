class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        str_set = set()
        for i in range(len(s)-k+1):
            str_set.add(str(s[i:i+k]))
        # print(str_set)
        for i in range(2**k):
            formatter = '{0:0%sb}'%(str(k))
            if formatter.format(i) not in str_set:
                return False
            
        return True
