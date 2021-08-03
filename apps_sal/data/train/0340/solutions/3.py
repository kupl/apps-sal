class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        lst = list([_f for _f in path.split("/") if _f])
        print(lst)
        stack = []

        for item in lst:
            if item == "..":
                if not stack:
                    continue
                stack.pop()
            elif item == ".":
                print("here")
                continue
            else:
                stack.append(item)

        return "/" + "/".join(stack)
