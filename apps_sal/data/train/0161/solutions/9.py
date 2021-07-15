class Solution:
     def isValidSerialization(self, preorder):
         """
         :type preorder: str
         :rtype: bool
         """   
         preorder, first = preorder.split(","), preorder.split(",")
         def backward(index):
             if index >= len(preorder) or index < 0: return 
             if index+1<len(preorder) and preorder[index+1] == preorder[index] == "#" and index-1 >= 0 and preorder[index-1] != "#":
                 preorder.pop(index)
                 preorder.pop(index)
                 preorder[index-1] = "#"
                 backward(index-2)
             else: backward(index+1)
         backward(0)
         return True if (preorder != first and preorder == ["#"]) or (preorder == first == ["#"]) else False
