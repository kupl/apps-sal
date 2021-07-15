class node:
    
    def __init__(self,val):
        
        self.val = val
        
        self.right = None
        
        self.left = None

class Solution:
    
    def update(self,i,j,ind,root):
    
        if i == j:
            root.val += 1
        else:
            
            mid = (i+j) // 2
            
            if ind <=mid:
                self.update(i,mid,ind,root.left)
            elif ind > mid:
                self.update(mid+1,j,ind,root.right)
                
            root.val = 0
            
            if root.left:
                root.val +=root.left.val
            if root.right:
                root.val += root.right.val
                
                
      
    def findSum(self,i,j,left,right,root):
        
        if left<=i and right>=j:
            return root.val
        
        elif right<i or left > j:
            return 0
        
        mid = (i+j) // 2
        
        if right<=mid:
            return self.findSum(i,mid,left,right,root.left)
        elif left>mid:
            return self.findSum(mid+1,j,left,right,root.right)
        
        else:
            
            x = self.findSum(i,mid,left,mid,root.left)
            
            y = self.findSum(mid+1,j,mid+1,right,root.right)
            
            return x+y
        
    
    def build(self,i,j):
        
        if i == j:
            root = node(0)
            
        else:
            
            mid = (i+j) // 2
            root = node(0)
            root.left = self.build(i,mid)
            root.right = self.build(mid+1,j)
            
            
            
            if root.left:
                root.val+=root.left.val
                
            if root.right:
                root.val+=root.right.val
                
                
        return root
            
   
    def solve(self,rating):
        n = max(rating) + 1
        
        self.arr = [0]*n
        
        length = len(rating)
        
        left = [0]*length
        right = [0]*length
        rootLeft = self.build(0,n)
        rootRight = self.build(0,n)
        
        
        for i in range(length):
            
            left[i] = self.findSum(0,n,0,rating[i]-1,rootLeft)
            self.update(0,n,rating[i],rootLeft)
                
        for i in range(length-1,-1,-1):
            
            right[i] = self.findSum(0,n,rating[i]+1,n,rootRight)
            self.update(0,n,rating[i],rootRight)
            
        
        ans = 0
        for i in range(1,length-1):
            
            ans = ans + left[i]*right[i]
        
        # print(left)
        # print(right)
        # print(\"************\")
        return ans
        
    def numTeams(self, rating: List[int]) -> int:
        
        if len(rating)<3:
            return 0
        
        temp = rating[:]
        temp.sort()
        
        value = 1
        
        self.mp = {}
        
        for x in temp:
            
            if x not in self.mp:
                
                self.mp[x] = value
                
                value +=1
                
            
        for i in range(len(rating)):
            
            rating[i] = self.mp[rating[i]]
            
            
        
        ans = self.solve(rating)+self.solve(rating[::-1])
        
        return ans
        
        

