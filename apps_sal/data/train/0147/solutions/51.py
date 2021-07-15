from queue import PriorityQueue

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        if k == 1:
            return max([speed[i] * efficiency[i] for i in range(n)]) % mod
        
        engs = sorted([(efficiency[i] % mod, speed[i] % mod) for i in range(n)])
        maxi = 0
        others = PriorityQueue()
        otherSum = 0
        for i in range(n - 1, -1, -1):
            maxi = max(maxi, ((engs[i][1] + otherSum) * engs[i][0]) )
            otherSum += engs[i][1]
            others.put(engs[i][1])
            while others.qsize() > k - 1:
                otherSum -= others.get()
            
        return maxi % mod
