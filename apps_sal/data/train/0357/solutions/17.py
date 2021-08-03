class Solution:
    def maxDistToClosest(self, arr):
        n = len(arr)
        start = 0  # start index of group of consecutive 0s
        end = 0  # end index of group of consecutive 0s

        maxdist, dist = 0, 0

        i = 0
        while (i < n):

            while (i < n and arr[i] == 1):
                i += 1
            start = i

            while (i < n and arr[i] == 0):
                i += 1
            end = i - 1

            if(start == 0):
                dist = end + 1
            elif(end == n - 1):
                dist = n - 1 - start + 1
            else:
                dist = (end - start) // 2 + 1
            maxdist = max(maxdist, dist)

        return maxdist
