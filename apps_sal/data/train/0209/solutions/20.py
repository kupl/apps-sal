class Solution:
    def mergeStones(self, stones, k):

        # quick check to see if this number of piles can be merged.
        if (len(stones) - 1) % (k - 1):
            return -1

        cost = [[None] * len(stones) for _ in stones]

        def subCost(left, right):

            # Base case: there is no cost to \"merging\" one pile
            if left == right:
                return 0

            if cost[left][right] != None:
                return cost[left][right]

            # Base case: a single merge is just the sum of the elements.
            if (right - left + 1) == k:
                cost[left][right] = sum(stones[left:right + 1])
                return cost[left][right]

            # find k-1 division points.  Each division except the last is the start index of a sub-array
            # ie. if stones = [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ], left = 0 right = 8 divs = [0, 3, 8, 9]
            # then sub-arrays are as follows: [0, 1, 2] [3, 4, 5, 6, 7]  [8]
            # the above divs would incidentally be valid for k = 3.

            divs = [left + i for i in range(k + 1)]
            divs[-1] = right + 1  # set the last divider to one past the subarray.
            # for example above, divs is initialized to -> [0, 1, 2, 9].  The first and last divider never change

            def moveDividers():
                # loop through dividers to move, starting at last one.
                # if the last one is at the end, move the next one up.

                def moveDivider(i):
                    if i == 0:
                        return False

                    # if the div we're looking at is smashing all dividers to its right against the right end of the array.
                    # If k = 3, i = 1, we have 1 divider to our right.  Leave 1 space for each divider to our right.
                    # division 0 stays at 0
                    # div 1 can go to 2.  = right - (k - 1 - i)
                    if divs[i] == (right - (k - 1 - i)):
                        # switch to the next divider to the left
                        return moveDivider(i - 1)

                    # move this divider to the next usable spot given where the left neighbor div is.
                    divs[i] += 1
                    while (divs[i] - divs[i - 1] - 1) % (k - 1):
                        divs[i] += 1

                    # stack all following divs next to each other and this one. []
                    for j in range(i + 1, len(divs) - 1):
                        divs[j] = divs[j - 1] + 1

                    return True

                # start by moving the rightmost divider
                return moveDivider(len(divs) - 2)

            best = float('inf')
            while 1:
                subSum = 0
                for div_i in range(len(divs) - 1):
                    subSum += subCost(divs[div_i], divs[div_i + 1] - 1)
                best = min(best, subSum)
                if not moveDividers():
                    break

            result = best + sum(stones[left:right + 1])
            cost[left][right] = result
            return result

        result = subCost(0, len(stones) - 1)
        # print(cost)
        return result
