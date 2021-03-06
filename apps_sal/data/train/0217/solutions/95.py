class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        result = set()
        curr = set()
        for num in A:
            curr = {num | prev_num for prev_num in curr}
            curr.add(num)
            result.update(curr)
        return len(result)
