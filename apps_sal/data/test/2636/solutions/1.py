class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

#         def get_height_end(idx, height):
#             # print(heightends)
#             for left, right in heightends[height]:
#                 if left <= idx < right:
#                     return right

#         coords1 = []
#         for left, right, height in buildings:
#             coords1.append(left)
#             coords1.append(right)
#         coords1.sort()

#         coords = []
#         for k, g in itertools.groupby(coords1):
#             coords.append(k)

#         index = { num: idx for idx, num in enumerate(coords) }
#         events = collections.defaultdict(list)
#         heightends = collections.defaultdict(list)

#         for left, right, height in buildings:

#             i = index[left]
#             while i < index[right]:
#                 # print(i, events, left, right)
#                 if events[i] != [] and sorted(events[i])[-1] >= height:
#                     i = get_height_end(i, sorted(events[i])[-1])
#                     continue

#                 events[i].append(height)
#                 i += 1
#             heightends[height].append([index[left], index[right]])

#         infpoints = []
#         prevheight = 0
#         for coord in coords:
#             coordheights = sorted(events[index[coord]])
#             coordheight = 0
#             if coordheights != []:
#                 coordheight = coordheights[-1]
#             if prevheight != coordheight:
#                 infpoints.append([coord, coordheight])
#                 prevheight = coordheight

#         return infpoints

        edges = []
        events = collections.defaultdict(list)
        for left, right, height in buildings:
            edges.append((left, -height, right))
            edges.append((right, 0, None))
            # heapq.heappush(events[left].append()
            # events[right].append((left, right, height))

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
