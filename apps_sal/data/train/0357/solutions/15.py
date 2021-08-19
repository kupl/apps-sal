class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        '''
        need to find the distance of the closest neighbor at each seat
        need to find distance to left and right neighbor at each seat 
        get the min of the two
        '''
        n = len(seats)
        distance = [-1] * n
        # calc distance to left neighbor
        left_neighbor = -float('inf')
        for seat in range(n):
            if seats[seat] == 1:
                left_neighbor = seat
            distance[seat] = seat - left_neighbor
        print(distance)
        # calc distance to right neighbor
        right_neighbor = float('inf')
        answer = 0
        for seat in range(n - 1, -1, -1):
            if seats[seat] == 1:
                right_neighbor = seat
            distance[seat] = min(distance[seat], right_neighbor - seat)
            # if distance[seat] > distance[answer]:
            #     answer = seat
        print(distance)
        return max(distance)
