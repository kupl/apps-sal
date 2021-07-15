
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        duplicates=[k*i for i in 'abcdefghijklmnopqrstuvwxyz']
        counter=0
        while counter!=len(s):
            counter=len(s)
            for i in duplicates:
                s=s.replace(i,'')
                
        return s
