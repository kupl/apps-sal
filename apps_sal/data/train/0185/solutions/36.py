class Solution:
    
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 2**k
        _new = set()
        for i in range(len(s)-k+1):
            var = s[i:i+k]
            if var not in _new:
                _new.add(var)
                need -= 1
            if need == 0:
                return True
        return False

