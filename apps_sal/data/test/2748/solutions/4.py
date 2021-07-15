class Solution:
     def letterCombinations(self, digits):
         """
         :type digits: str
         :rtype: List[str]
         """
         if digits==None or len(digits) ==0:
             return []
         res=[]
         cur=""
         dmap={}
         dmap["0"]=[" "]
         dmap["1"]=[]
         dmap["2"]=["a","b","c"]
         dmap["3"]=["d","e","f"]
         dmap["4"]=["g","h","i"]
         dmap["5"]=["j","k","l"]
         dmap["6"]=["m","n","o"]
         dmap["7"]=["p","q","r","s"]
         dmap["8"]=["t","u","v"]
         dmap["9"]=["w","x","y","z"]
         self.dfs(digits,dmap,0,cur,res)
         return res
     
     def dfs(self,digits,dmap,idx,cur,res):
         if idx ==len(digits):
             res.append(cur)
             return
         else:
             c=digits[idx]
             for i in dmap[c]:
                 self.dfs(digits,dmap,idx+1,cur+i,res)

