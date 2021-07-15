class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        container = [0]
        for num in A:
            container.append(container[-1] + num)
            
        count = Counter()
        
        ans = 0
        for num in container:
            # if count at num empty, just adds 0
            ans += count[num]
            # puts num + S into count with a count of 1 or increments num + S by 1
            count[num+S] += 1
        
        return ans

