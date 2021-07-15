class Solution:
     def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        memo = collections.defaultdict(int)
        def maxUncrossedLinesHelper(ai:int, bi:int)->int:
            result = 0
            if ai >= len(A): return 0
            if bi >= len(B): return 0
            if (ai,bi) in memo: return memo[(ai,bi)]
            
            if A[ai] == B[bi]:
                result = maxUncrossedLinesHelper(ai+1, bi+1) + 1
                memo[(ai,bi)] = result
         ##       return result            
            
            chooseA = 0
            try:
                ainb = B.index(A[ai], bi)
            except:
                ainb = -1

            if ainb > 0:
                chooseA = maxUncrossedLinesHelper(ai+1, ainb+1) + 1

            chooseB = 0
            try:
                bina = A.index(B[bi], ai)
            except:
                bina = -1

            if bina > 0:
                chooseB = maxUncrossedLinesHelper(bina+1, bi+1) + 1

            notchooseAB = maxUncrossedLinesHelper(ai+1, bi+1)

            result = max(chooseA, chooseB, notchooseAB,result)
            memo[(ai,bi)] = result
            return result
        
        result = maxUncrossedLinesHelper(0, 0)
        return result

