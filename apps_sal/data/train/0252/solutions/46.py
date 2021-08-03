class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        covers = []
        for i, r in enumerate(ranges):
            if r == 0:
                continue
            covers.append([max(0, i - r), min(n, i + r)])

        if len(covers) == 0:
            return -1

        covers.sort(key=lambda x: x[0])

        result = 0
        reach = 0
        while len(covers) != 0:
            temp = None
            while len(covers) != 0:
                if covers[0][0] - reach > 0:
                    break
                x = covers.pop(0)
                if temp == None or temp[1] < x[1]:
                    temp = x

            if temp is None:
                return -1
            result += 1
            reach = temp[1]
            if reach == n:
                break

        return result
