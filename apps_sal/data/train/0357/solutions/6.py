class Solution:
    def maxDistToClosest(self, seats) -> int:
        self.dists = [0 for i in range(len(seats))]
        i = 0
        while i < len(seats) - 1:
            i = self.assign_weights(i, seats)
        return max(self.dists)

    def assign_weights(self, start, seats):
        if start == 0 and seats[start] != 1:
            l_seat = math.inf
        else:
            l_seat = start
        temp = start + 1
        while temp < len(seats) and seats[temp] != 1:
            temp += 1

        if temp == len(seats):
            r_seat = math.inf
        else:
            r_seat = temp

        for i in range(start, min(len(seats), r_seat)):
            l_dist = abs(l_seat - i)
            r_dist = r_seat - i
            self.dists[i] = min(l_dist, r_dist)

        return r_seat
