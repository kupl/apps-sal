class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.solv(n, k)
    
    def solv(sef, n, k):
        i = 1
        lst = ['0']
        ans = '0'
        ki = 1
        if k == 1:
            return '0'
        while i < n+1:
            ans = '1'
            lst.append(ans)
            ki += 1
            if ki == k:
                return ans
            for j in range(ki-2,-1,-1):
                ans = '1' if lst[j] == '0' else '0'
                lst.append(ans)
                ki += 1
                if ki == k:
                    return ans
            i += 1
        return None
