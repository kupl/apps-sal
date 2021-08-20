class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        """ DP causing timeout 
        def get_max_force(pos, count):

            #print(f"get_max_force pos_index {pos} posistion {position[pos]} count {count}")
            if count <=1 :
                return float('inf')

            if dp[pos][count-1] > -1: 
                #print("saved time")
                return dp[pos][count-1] 

            if n - pos == count:
                min_force = float('inf')
                for pos_index in range(pos+1, n):
                    min_force = min(min_force, position[pos_index]-position[pos_index-1])
                #print(f"dp 3 pos_index {pos} position {position[pos]} count{count} : {dp[pos][count-1]}")  
                dp[pos][count-1] = min_force
                return min_force

            if count == 2:
                dp[pos][count-1] = position[-1] - position[pos]
                #print(f"dp 2 pos_index {pos} position {position[pos]} position[-1] {position[-1]} count{count} : {dp[pos][count-1]}")
                return dp[pos][count-1]

            max_force = 0

            for pos_index in range(pos+1, n):
                if n - pos_index < count - 1:
                    break
                max_force = max(max_force, min(position[pos_index]-position[pos], get_max_force(pos_index, count-1)))

            dp[pos][count-1] = max_force
            #print(f"dp 1 pos_index {pos} position {position[pos]} count{count} : {max_force}")
            return max_force

        n = len(position)
        position.sort()
        dp = [[-1] * m for _ in position]
        if m == n:
            return get_max_force(0, m)            

        if m == 2:
            return position[-1] - position[0]


        max_force = 0       
        for pos_index in range(0, n):
            max_force = max(max_force, get_max_force(pos_index, m))

        return max_force
        """
        n = len(position)
        position.sort()

        def calc(d):
            curr = position[0]
            ans = 1
            for i in range(1, n):
                if position[i] - curr >= d:
                    index = i
                    curr = position[i]
                    ans += 1
            return ans
        (l, r) = (0, position[-1] - position[0])
        d = 0
        while l < r:
            mid = l + (r - l) // 2
            count = calc(mid)
            if count < m:
                r = mid
            else:
                l = mid + 1
            ' \n            if count < m:\n                r = mid - 1\n            elif count >= m:\n                l = mid\n            '
        if calc(l) == m:
            return l
        else:
            return l - 1
