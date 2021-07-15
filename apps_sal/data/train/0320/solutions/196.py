class Solution:
    def minOperations(self, a: List[int]) -> int:
        
        ans = 0
        
        while True:
            a.sort(reverse = True)
            for i in range(len(a)):
                if a[i]%2:
                    ans += 1
                    a[i] -= 1
            for i in a:
                if i != 0:
                    break
            else:
                break
            for i in range(len(a)):
                if a[i]%2 == 0:
                    a[i] //= 2
            ans += 1
            
        return ans
