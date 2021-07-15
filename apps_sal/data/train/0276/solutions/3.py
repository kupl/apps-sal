class Solution:
     def findMinStep(self, board, hand):
         """
         :type board: str
         :type hand: str
         :rtype: int
         """
         hmap=collections.defaultdict(int)
         for c in hand:
             hmap[c]+=1
         res=float("inf")
         res=self.helper(board,hmap)
         if res==float("inf"):
             return -1
         return res
     
     def helper(self,board,hmap):
         board=self.removeContinues(board)
         if len(board) ==0:
             return 0
         j=0
         res=float("inf")
         for i in range(len(board)+1):
             if i<len(board) and board[i]==board[j]:
                 continue
             need=3-(i-j)
             if hmap[board[j]]>=need:
                 hmap[board[j]]-=need
                 nxtCnt=self.helper(board[0:j]+board[i:],hmap)
                 if nxtCnt!=float("inf"):
                     res=min(res,nxtCnt+need)
                 hmap[board[j]]+=need
             j=i
         return res
         
     def removeContinues(self,board):
         j=0
         for i in range(len(board)+1):
             if i<len(board) and board[i]==board[j]:
                 continue
             if i-j>=3:
                 return self.removeContinues(board[0:j]+board[i:])
             else:
                 j=i
         return board
         

