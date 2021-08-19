class Solution:

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        (stack, preorder) = ([], preorder.split(','))
        top = -1
        for s in preorder:
            stack.append(s)
            top += 1
            while self.endsWithTwoHashes(stack, top):
                (h, top) = (stack.pop(), top - 1)
                (h, top) = (stack.pop(), top - 1)
                if top < 0:
                    return False
                stack[-1] = '#'
        return len(stack) == 1 and stack[0] == '#'

    def endsWithTwoHashes(self, stack, top):
        if top < 1:
            return False
        if stack[top] == '#' and stack[top - 1] == '#':
            return True
        return False
