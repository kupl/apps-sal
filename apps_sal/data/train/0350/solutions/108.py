from collections import Counter


class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        (equalCt, lessCt) = (Counter(), Counter())
        (equalPt, lessPt) = (0, 0)
        res = 0

        def add_to_counter(x, co):
            co[x] += 1

        def subtr_from_counter(x, co):
            co[x] -= 1
            if co[x] == 0:
                del co[x]
        for (right, num) in enumerate(A):
            add_to_counter(num, equalCt)
            add_to_counter(num, lessCt)
            while len(equalCt) > K:
                subtr_from_counter(A[equalPt], equalCt)
                equalPt += 1
            while len(lessCt) >= K:
                subtr_from_counter(A[lessPt], lessCt)
                lessPt += 1
            res += lessPt - equalPt
        return res
