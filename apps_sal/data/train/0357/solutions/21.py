from bisect import bisect


class Solution:

    def maxDistToClosest(self, seats: List[int]) -> int:
        occupied_indexes = []
        empty_indexes = []
        for (i, is_occupied) in enumerate(seats):
            if is_occupied:
                occupied_indexes.append(i)
            else:
                empty_indexes.append(i)
        num_occupied = len(occupied_indexes)
        max_distance = 1
        coi = 0
        for empty_index in empty_indexes:
            while coi < num_occupied and occupied_indexes[coi] < empty_index:
                coi += 1
            ridx = coi
            lidx = ridx - 1
            lmd = rmd = float('inf')
            if lidx >= 0:
                lmd = empty_index - occupied_indexes[lidx]
            if ridx < num_occupied:
                rmd = occupied_indexes[ridx] - empty_index
            max_distance = max(max_distance, min(lmd, rmd))
        return max_distance
