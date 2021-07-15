class Solution:
    # def hasAllCodes(self, s: str, k: int) -> bool:
    #     target_len = len(bin(k))-2
    #     for target in range(k, -1, -1):
    #         target = bin(target)[2:]
    #         target = (target_len-len(target))*'0'+target
    #         print (target)
    #         if s.find(target)==-1:
    #             return False
    #     return True
    
    def hasAllCodes(self, s: str, k: int) -> bool:
        d = set()
        for i in range(len(s)-k+1):
            if s[i:i+k] not in d:
                d.add(s[i:i+k])
                if len(d)==2**k:
                    return True
        print (d)
        return False    
