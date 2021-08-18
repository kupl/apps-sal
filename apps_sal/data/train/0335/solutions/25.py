import collections


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        recorder = {0: 0}
        for rod in rods:
            generateRecorder = collections.defaultdict(int)
            for record in recorder:
                largeNum = recorder[record]
                generateRecorder[record] = max(generateRecorder[record], largeNum)
                generateRecorder[record + rod] = max(generateRecorder[record + rod], largeNum + rod)
                generateRecorder[abs(rod - record)] = max(generateRecorder[abs(rod - record)], max(largeNum, largeNum - record + rod))
            recorder = generateRecorder
        return recorder[0]
