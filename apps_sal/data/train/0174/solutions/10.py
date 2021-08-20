class Solution:

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        max_len = 0
        depth2len = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                max_len = max(max_len, depth2len[depth] + len(name))
            else:
                depth2len[depth + 1] = depth2len[depth] + len(name) + 1
        return max_len
