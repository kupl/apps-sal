class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        l1=list(s1)
        l2=list(s2)
        l1.sort()
        l2.sort()
        count=0
        count1=0
        for i in range(len(l1)):
            if l1[i]>=l2[i]:
                count+=1
        if count==len(l1):
            return True
        for i in range(len(l2)):
            if l2[i]>=l1[i]:
                count1+=1
        if count1==len(l1):
            return True
        return False

