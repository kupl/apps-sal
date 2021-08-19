class Solution:

    def countTriplets(self, A: List[int]) -> int:
        and_values = {}
        for x in A:
            for y in A:
                c = x & y
                if c in and_values:
                    and_values[c] += 1
                else:
                    and_values[c] = 1
        triplet_count = 0
        for a in and_values:
            for z in A:
                if a & z == 0:
                    triplet_count += and_values[a]
        return triplet_count
