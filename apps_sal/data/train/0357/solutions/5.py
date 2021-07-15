class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        seated = [i for i, elem in enumerate(seats) if elem == 1]
        empties = [i for i, elem in enumerate(seats) if elem == 0]
        
        s_p, e_p = 0, 0
        min_dist = 0
        while e_p < len(empties):
            # make the determination:
            while (s_p < len(seated) - 1) and empties[e_p] > seated[s_p]:
                s_p += 1
            if s_p > 0:
                tmp_dist = min(abs(empties[e_p] - seated[s_p - 1]), 
                               abs(empties[e_p] - seated[s_p]))
            else:
                tmp_dist = abs(empties[e_p] - seated[s_p])
            if tmp_dist > min_dist:
                min_dist = tmp_dist
            e_p += 1
        return min_dist
