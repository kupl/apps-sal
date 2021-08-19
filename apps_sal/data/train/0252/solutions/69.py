class Solution:

    def minTaps(self, n: int, ranges) -> int:

        def process_input(ranges):
            spans = []
            for i in range(len(ranges)):
                spans.append([max(i - ranges[i], 0), i + ranges[i]])
            return spans
        spans = process_input(ranges)
        spans.sort(key=lambda time: (time[0], -time[1]))
        sol = []
        step = 0.5
        for i in range(len(spans)):
            if step > n:
                continue
            if spans[i][0] < step and spans[i][1] > step:
                try:
                    if spans[i][0] <= sol[-2][1]:
                        sol.pop()
                except:
                    pass
                sol.append(spans[i])
                step = spans[i][1] + 0.5
        if step < n:
            return -1
        return len(sol)
