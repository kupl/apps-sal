class Solution:
    def totalFruit(self, tree: List[int]) -> int:
    
        out = 0
        for i in range(len(tree)):
            tot = self.getTotalAtIndex(tree, i)
            if tot>out:
                out = tot
            if tot == len(tree):
                break
        return out
    
    
    def getTotalAtIndex(self, tree, i):
        
        fruit_types = set()
        cnt = 0
        for j in range(i, len(tree)):
            if len(fruit_types)<2:
                fruit_types.add(tree[j])
                
            if tree[j] in fruit_types:
               cnt+=1
            else:
                break
        return cnt
        pass

