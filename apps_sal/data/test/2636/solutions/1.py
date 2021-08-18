class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        edges = []
        events = collections.defaultdict(list)
        for left, right, height in buildings:
            edges.append((left, -height, right))
            edges.append((right, 0, None))

        pq = [(0, float('inf'))]
        edges.sort()
        skyline = [(0, 0)]

        for edge, height, right in edges:

            while edge >= pq[0][1]:
                heapq.heappop(pq)
            if height:
                heapq.heappush(pq, (height, right))
            if skyline[-1][1] != -pq[0][0]:
                skyline.append([edge, -pq[0][0]])
        return skyline[1:]
