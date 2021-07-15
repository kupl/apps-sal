class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        # 12:57 8/24/20
        
        cur, res = set(),set()
        for num in A:
            cur = {num | j for j in cur} | {num}
        #     res |= cur
            # cur = set(num | k for k in A)
            # cur.add(num)
            res.update(cur)
        
        return len(res)
        
        
                
        # res, cur = set(), set()
        # for i in A:
        #     cur = {i | j for j in cur} | {i}
        #     res |= cur
        # return len(res)

            
                

