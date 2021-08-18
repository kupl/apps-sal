class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if len(preorder) < 1:
            return False

        stack = []
        for s in preorder.split(','):
            stack.append(False)
            if s == '
               while len(stack) > 2 and stack[-2]:
                    stack.pop()
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(True)

        return stack == [False, True]
