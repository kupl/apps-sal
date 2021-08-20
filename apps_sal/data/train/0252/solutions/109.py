class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        areas = [(x - ranges[x], x + ranges[x]) for x in range(n + 1)]
        areas = sorted(areas, key=lambda x: x[0])

        def get_intersections(current, intervals):
            results = []
            for interval in intervals:
                if current[0] <= interval[0] <= current[1] and interval[1] > current[1]:
                    results.append(interval)
            return results
        first = areas[0]
        for intersection in areas:
            if intersection[0] <= 0 and intersection[1] > first[1]:
                first = intersection
        selected = [first]
        area_to_cover = (first[1], n)
        while area_to_cover[0] < area_to_cover[1]:
            prev = selected[-1]
            intersections = get_intersections(prev, areas)
            if len(intersections) is 0:
                return -1
            intersections = sorted(intersections, key=lambda x: x[1])
            rightmost = intersections[-1]
            if rightmost[1] < area_to_cover[0]:
                return -1
            selected.append(rightmost)
            area_to_cover = (rightmost[1], n)
        return len(selected)
