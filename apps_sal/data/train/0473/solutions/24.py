class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        triplets = 0

        # rangeXOR[i,j] stores XOR of elements from arr[i] to arr[j] (both incl), i<j
        #rangeXOR = []
        for i, a in enumerate(arr):
            # tackle sub arrays starting at arr[i]
            subrange = []

            for j, b in enumerate(arr[i:]):
                j_absolute = i + j

                if j_absolute == i:
                    subrange.append(b)
                else:  # j_absolute > i
                    subrange.append(subrange[-1] ^ b)

                if subrange[-1] == 0:
                    # output all triplets here
                    triplets += j  # j_absolute - i

            # rangeXOR.append(subrange)

        return triplets
