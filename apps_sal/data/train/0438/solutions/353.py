# union find problem
class UnionNode:
    def __init__(self,value,parent=None):
        self.value = value
        self.parent = parent
        self.size = 1
        
class UnionFind:
    def __init__(self):
        return
    
    def findGroup(self,curNode):
        while(curNode!=curNode.parent):
            curNode = curNode.parent
        return curNode
    
    def merge(self,node1,node2):
        root1,root2 = self.findGroup(node1),self.findGroup(node2)
        if(root1==root2):
            return -1
        if(root1.size>root2.size):
            root2.parent = root1
            root1.size += root2.size
            return root1.size
        else:
            root1.parent = root2
            root2.size += root1.size
            return root2.size
            
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        numOfm = 0
        res = -1
        string = [UnionNode(0) for _ in range(len(arr))]
        theUnionFind = UnionFind()
        for i in range(len(arr)):
            step = i+1
            loc = arr[i]-1
            thisUnionNode = string[loc]
            thisUnionNode.value = 1
            thisUnionNode.parent = thisUnionNode
            thisSize = 1
            if(loc-1>=0 and string[loc-1].value==1):
                # merge with left nei
                
                # if left nei has size m, numOfm -= 1
                newSize = theUnionFind.merge(string[loc-1],string[loc])
                if(newSize-thisSize==m):
                    numOfm -= 1
                thisSize = newSize
            if(loc+1<len(string) and string[loc+1].value==1):
                # merge with right nei
                
                # if right nei has size m, numOfm -= 1
                newSize = theUnionFind.merge(string[loc+1],string[loc])
                if(newSize-thisSize==m):
                    numOfm -= 1
                thisSize = newSize
            #print(thisSize)
            if(thisSize==m):
                numOfm += 1
            if(numOfm > 0):
                res = step
        
        return res
        
        
        
        

