class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        if len(A) % 2 == 1:
            return False
        
        count = collections.defaultdict(int)
        for num in A:
            count[num] += 1
        A.sort()
        for num in A:
            if count[num] > 0:
                double = num * 2
                if double in count and count[double] > 0:
                    # print(\"found\", double)
                    count[num] -= 1                    
                    count[double] -= 1
                    
        for num in count:
            if count[num] != 0:
                return False
        return True
            

