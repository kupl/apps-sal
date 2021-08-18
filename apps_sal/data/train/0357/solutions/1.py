class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        anspointer = -float('inf')
        prvpointer = None

        for i, seat in enumerate(seats):

            if seat == 1:
                if prvpointer == None:
                    anspointer = i
                else:
                    anspointer = max(anspointer, (i - prvpointer) // 2)

                prvpointer = i

        anspointer = max(anspointer, len(seats) - 1 - prvpointer)

        return anspointer
