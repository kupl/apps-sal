class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        if A == []:
            return 0
        # count = [0]
        # dic = {}
        # def OR(s):
        #     if len(s) == 1:
        #         return s[0]
        #     res = s[0]
        #     for item in s[1:]:
        #         res = res | item
        #     return res
        # for i in range(len(A)):
        #     for j in range(i, len(A)):
        #         res = OR(A[i:j+1])
        #         if res in dic:
        #             continue
        #         dic[res] = 0
        #         count[0] += 1
        # return count[0]
        my_set = set(A)
        curr = 0
        prev = set()
        prev.add(A[0])
        for num in A[1:]:
            temp = set()
            for p in prev:
                temp.add(num | p)
                my_set.add(num | p)
            prev = temp
            prev.add(num)

        return len(my_set)
