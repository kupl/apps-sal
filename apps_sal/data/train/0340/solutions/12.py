class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        stack = []
        for n in path:
            if n == "" or n == ".":
                continue
            elif n == "..":
                if stack != []:
                    stack.pop()
            else:
                stack.append(n)

        return "/" + '/'.join(stack)
