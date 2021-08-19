class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        triplets = 0
        for (i, a) in enumerate(arr):
            subrange = []
            for (j, b) in enumerate(arr[i:]):
                j_absolute = i + j
                if j_absolute == i:
                    subrange.append(b)
                else:
                    subrange.append(subrange[-1] ^ b)
                if subrange[-1] == 0:
                    triplets += j
        return triplets
