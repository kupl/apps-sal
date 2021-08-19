class Solution:
    def maxDistToClosest(self, seats) -> int:
        self.dists = [0 for i in range(len(seats))]
        i = 0
        # loop thru seats, assign weights as they come. update i to next seat found
        while i < len(seats) - 1:
            i = self.assign_weights(i, seats)
        # print(self.dists)
        return max(self.dists)
    # from left seat, search for next seat and assign weights

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
