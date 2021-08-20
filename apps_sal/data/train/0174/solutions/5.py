class Solution:

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        max_line = 0
        path_size = {0: 0}
        lines = input.splitlines()
        for line in lines:
            stripped = line.lstrip('\t')
            depth = len(line) - len(stripped)
            if '.' in stripped:
                max_line = max(max_line, path_size[depth] + len(stripped))
            else:
                path_size[depth + 1] = path_size[depth] + len(stripped) + 1
        return max_line
