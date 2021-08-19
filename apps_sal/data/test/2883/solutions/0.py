class Solution:

    def merge(self, intervals):
        new_intervals = []
        for interval in sorted(intervals, key=lambda i: i.start):
            if new_intervals and interval.start <= new_intervals[-1].end:
                new_intervals[-1].end = max(new_intervals[-1].end, interval.end)
            else:
                new_intervals.append(interval)
        return new_intervals
