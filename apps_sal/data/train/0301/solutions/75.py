class Solution:
  def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
    if len(A) > len(B): return self.maxUncrossedLines(B, A)
    if not A or not B: return 0
#     try:
#       idx = B.index(A[0])
#       return max(1+self.maxUncrossedLines(A[1:], B[idx+1:]), self.maxUncrossedLines(A[1:], B))
#     except:
#       return self.maxUncrossedLines(A[1:], B)
      

# i = 0..len(A)-1    2  5 1 2 5
# j = 0..len(B)-1    10 5 2 1 5 2

    dp = [[0]*len(B) for _ in range(len(A))]
    indexB = collections.defaultdict(list)
    for i, num in enumerate(B):
      indexB[num].append(i)

    for i in reversed(list(range(len(A)))):
      for j in reversed(list(range(len(B)))):
        # find A[i] in B[j:]
        found = False
        for idx in indexB.get(A[i], []):
          if idx >= j: 
            found = True
            break

        if found:
          dp[i][j] = max(1+(dp[i+1][idx+1] if i+1<len(A) and idx+1<len(B) else 0), dp[i+1][j] if i+1<len(A) else 0)
        else:
          dp[i][j] = dp[i+1][j] if i+1 < len(A) else 0
    return dp[0][0]

