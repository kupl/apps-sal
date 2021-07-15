class Solution:
    def knightDialer(self, n: int) -> int:
        cnt = 0
        jump = [[4, 6], [6, 8], [7, 9], [4, 8], [
            0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        visited = dict()
        def helper(n,i):
            if (n,i) in visited:
                return visited[(n,i)]
            if n == 1:
                visited[(n,i)] = 1
                return 1
            tot = 0
            
            for v in jump[i]:
                tot += helper(n -1,v)
            visited[(n,i)] = tot
            return tot
        for i in range(10):
            cnt += helper(n,i)
        return cnt%(10**9 + 7)
                
        

