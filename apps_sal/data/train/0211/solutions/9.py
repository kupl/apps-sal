class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        lookup = set()
        return self.traverse(s, 0, lookup)
    
    def traverse(self, s, index, lookup):
        if index > len(s):
            return 0
        array = []
        for idx in range(index,len(s)+1):
            if len(s[index:idx])> 0 and s[index:idx] not in lookup:
                lookup.add(s[index:idx])
                array.append(1 + self.traverse(s, idx, lookup))
                lookup.remove(s[index:idx])
                
                
        return max(array)  if array else 0
