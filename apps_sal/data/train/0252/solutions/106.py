class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for (i, x) in enumerate(ranges):
            intervals.append([i - x, i + x])

        def mySortKey(x):
            left = x[0]
            if left <= 0:
                left = 0
            right = x[1]
            return left * 100 - right
        intervals.sort(key=mySortKey)
        print(intervals)
        greedyFurthest = intervals[0][1]
        nextGreedyFurthest = 0
        j = 0
        count = 1
        while j < len(intervals):
            connect = False
            if greedyFurthest >= n:
                return count
            while j < len(intervals) and intervals[j][0] <= greedyFurthest:
                if intervals[j][1] > nextGreedyFurthest:
                    nextGreedyFurthest = intervals[j][1]
                j += 1
                connect = True
            greedyFurthest = nextGreedyFurthest
            count += 1
            if not connect:
                return -1
        if greedyFurthest >= n:
            return count
        else:
            return -1
