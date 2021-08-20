class Solution:

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        edges = []
        for (left, right, height) in buildings:
            edges.append((left, -height, right))
            edges.append((right, 0, None))
        edges.sort()
        pq = [(0, float('inf'))]
        skyline = [(0, 0)]
        print(edges)
        for (left, negheight, right) in edges:
            while pq[0][1] <= left:
                heapq.heappop(pq)
            if negheight:
                heapq.heappush(pq, (negheight, right))
            if skyline[-1][1] != -pq[0][0]:
                skyline.append([left, -pq[0][0]])
        return skyline[1:]
