class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        MOD = 1000000007
        count = [0] * 101
        for x in A:
            count[x] += 1
        ans = 0
        for x in range(101):
            for y in range(x+1, 101):
                z = target - x - y
                if y < z <= 100:
                    ans += count[x] * count[y] * count[z]
                    ans %= MOD
        for x in range(101):
            z = target - 2*x
            if x < z <= 100:
                ans += count[x] * (count[x] - 1) // 2 * count[z]
                ans %= MOD
                
        for x in range(101):
            if (target - x) % 2 == 0:
                y = (target - x) // 2
                if x < y <= 100:
                    ans += count[x] * count[y] * (count[y] - 1) // 2
                    ans %= MOD
        
        if target % 3 == 0:
            x = target // 3
            if 0 <= x <= 100:
                ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                ans %= MOD
        return ans
