class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        result = set()
        curr = set()
        for num in A:
            curr = {num | prev_num for prev_num in curr}
            curr.add(num)
            result.update(curr)
        return len(result)
        
        
        
#         result = set()
#         prev = set([0])
#         for num in A:
#             curr = set([num])
#             for prev_num in prev:
#                 curr.add(prev_num | num)
#             result |= curr
#             prev = curr
#         return len(result)

