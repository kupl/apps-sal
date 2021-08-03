class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # Goal is to maximize 0's on each side of i
        # so first option that immediatly comes to mind is to run through the list
        # checking every positon, and then its distance, saving the seat with the maximized distance
        # This is really slow
        # to speed it up, i can only check seats that are farther from most recent seat than best yet
        # so in the first example

        # [1,0,0,0,1,0,1]
        # 0 continue
        # 1, check its 1 away, save its values
        # 2 check its two away, save its values
        # 3 its 3 away check its values, do not save
        # 4 continue
        # 5 1 is most recent continue
        # 6 conitnue

        # still n^2 but faster than checking EVERY possibiliy

        # Go through once, saving the position of every person initially.

        # So here we just have to loop through and find the max difference between. Then return the mid value
        # This algorithm is much faster

        # Edge case of best seat being on far right and far left
        # first find distance of first person from beginning, then afyer

        # 0, 4, 6
        # best = people[0]
        # pos = 0
        # distance = (people[i] - people[i-1])//2
        # if distance > best:
        #   best = distance
        #
        # [0, 0, 1]
        prev = -1
        best = 0
        for i in range(0, len(seats)):
            if seats[i] == 1:
                if prev == -1:
                    distance = i
                else:
                    distance = (i - prev) // 2
                best = max(best, distance)
                prev = i
        best = max(best, len(seats) - prev - 1)

#         best = people[0]

#         for i in range(1, len(people)):
#             distance = (people[i] - people[i-1])//2
#             best = max(best, distance)

#         best = max(best, len(seats) - people[-1]-1)
        return best
