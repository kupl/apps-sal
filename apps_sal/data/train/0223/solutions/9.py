class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        # my solution......beat 100 %

        l = len(citations)
        if l == 0:
            return 0          # shit testcase: []
        if l == 1:
            if citations[0] == 0:
                return 0          # shit testcase: [0]
            else:
                return 1          # for testcase: [1], [2] or [100] etc...
        if min(citations) >= l:
            return l          # for testcase: [2,3], [5,8], [3,4,5], [7,8,9,9] etc...

        citations = citations[::-1]
        count = 0
        thres = 0                                   # (count, thres): this author has "count" articles with citations >= thres
        i = 0
        while i < len(citations):
            if thres >= count:
                thres = citations[i]
                count += 1
                i += 1
            else:
                return count - 1
        return count - 1
