class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        L = len(arr)
        works = [0] * L
        not_works = [0] * L
        if arr[0] % 2 == 1:
            works[0] += 1
        else:
            not_works[0] += 1
        for i in range(1, L):
            if arr[i] % 2 == 0:
                works[i] += works[i - 1]
                not_works[i] += not_works[i - 1]
            else:
                works[i] += not_works[i - 1]
                not_works[i] += works[i - 1]
            if arr[i] % 2 == 1:
                works[i] += 1
            else:
                not_works[i] += 1
        return sum(works) % (10 ** 9 + 7)
