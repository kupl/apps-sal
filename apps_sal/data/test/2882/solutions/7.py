class Node(object):
    def __init__(self,val,root,n,p):
        self.val=val
        self.n=n
        self.p=p
        if root:
            self.root=root
        else:
            self.root=self
        self.left=self.leftchild(n,p)
        self.right=self.rightchild(n,p)
           
    def leftchild(self,n,p):
        if n==0:
            if p==0:                 
                temp=''.join(self.val);
                self.root.val.append(temp)
            return None

        if n>0:
            return Node(self.val+['('],self.root,n-1,p+1)

    def rightchild(self,n,p):
        if p==0:
              return None
        else:
              return Node(self.val+[')'],self.root,n,p-1)
            

class Solution:
    def generateParenthesis(self, s):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        D=Node([],None,s,0)
        return D.val

        
               