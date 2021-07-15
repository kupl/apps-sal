class Solution:
    def countTriplets(self, A: List[int]) -> int:
        res = cur = 0
        count = {0: [1, 0]}
        for i, a in enumerate(A):
            cur ^= a
            n, total = count.get(cur, [0, 0])
            res += i * n - total
            count[cur] = [n + 1, total + i + 1]
        return res
            
            

