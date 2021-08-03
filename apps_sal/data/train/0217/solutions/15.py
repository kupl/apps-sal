class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        results = set()
        temp = {0}
        for cur in A:
           # print(temp)
            temp = {cur} | {cur | t for t in temp}
            results.update(temp)
        return len(results)
