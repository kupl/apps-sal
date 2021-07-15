class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        self.ans = 0
        vis = set()
        def help(s, i):
            if len(s)==len(set(s)):
                self.ans = max(self.ans, len(s))
            if i>=len(arr):
                return
            for j in range(i, len(arr)):
                if j not in vis:
                    vis.add(j)
                    help(s+arr[j], j+1)
                    vis.remove(j)
        help('',0)
        return self.ans
