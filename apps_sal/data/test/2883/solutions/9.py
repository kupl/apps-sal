# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        '''
        先按照每个会议的开始时间排序，用一个数列来保存会议，条件是
        如果当前会议的开始时间比数列中最后一个会议的结束时间还晚，另起炉灶。
        如果开始时间比结束时间还早，挤进去！比较会议的结束时间，更新。
        '''
        intervals.sort(key=lambda x : x.start)
        res = []
        for interval in intervals:
            # 如果res 是空的，初始化的情况，要把第一个会议加进去！
            if not res or interval.start > res[-1].end:
                res.append(interval)
            else:
                res[-1].end = max(interval.end, res[-1].end)
        return res
        