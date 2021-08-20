class Solution:

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        lines = input.split('\n')
        paths = []
        ans = 0
        for line in lines:
            name = line.strip('\t')
            depth = len(line) - len(name)
            if '.' not in name:
                if depth >= len(paths):
                    paths.append(len(name) + 1)
                else:
                    paths[depth] = len(name) + 1
            else:
                ans = max(ans, sum(paths[:depth]) + len(name))
        return ans
