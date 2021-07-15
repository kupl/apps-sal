class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        table = collections.defaultdict(int)
        for num in A:
            table[num] += 1
        A.sort()
        for num in A:
            if table[num] == 0:
                continue
            pair = num * 2
            if num < 0:
                pair = num / 2
            if table[pair] < 1:
                return False
            table[num] -= 1
            table[pair] -= 1
        return True
            
            
                

