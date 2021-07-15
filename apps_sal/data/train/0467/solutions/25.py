class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0 
        
        for n in nums:
            st = set()
            for i in range(1, int(sqrt(n))+1):
                if n%i == 0:
                    st.add(i)
                    st.add(n//i)
            
            if len(st) == 4:
                ans += sum(st)
        
        return ans
