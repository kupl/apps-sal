class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        change = []
        if len(s)!=len(t):
            return False
        for a,b in zip(s,t):
            if a!=b:
                change.append(ord(b)-ord(a))
        for index,number in enumerate(change):
            if number < 0:
                change[index]+=26
        count = [0]*26
        for index,number in enumerate(count):
            count[index]+=int(k/26)
        remaining = k%26
        i=1
        for j in range(remaining):
            count[i]+=1
            i+=1
        for number in change:
            if count[number]==0:
                return False
            else:
                count[number]-=1
        return True
            

