class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        my_set = set(A)
        curr = 0
        prev = set()
        prev.add(A[0])
        for num in A[1:]:
            temp = set()
            curr |= num
            my_set.add(curr)
            prev.add(num)
            for p in prev:
                temp.add(num | p)
                my_set.add(num | p)
            prev = temp

        return len(my_set)
