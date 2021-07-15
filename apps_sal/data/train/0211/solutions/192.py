class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return get_max(s, set())
        
def get_max(s, set):
    maxi=0
    for i in range(1,len(s)+1):
        if s[:i] not in set:
            set.add(s[:i])
            # print(set)
            maxi=max(maxi, 1+get_max(s[i:],set))
            set.remove(s[:i])
            
    return maxi
