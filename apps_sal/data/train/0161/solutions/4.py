class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')

        if preorder[0] == '
           return len(preorder) == 1

        s = []

        curr = preorder[0]
        on_left = True

        for i in range(1, len(preorder)):
            if not curr:
                return False

            e = preorder[i]

            if e != '
               if on_left:
                    s.append(curr)

                curr = e
                on_left = True
            else:
                if not on_left:
                    curr = s.pop() if len(s) > 0 else None

                on_left = False

        return curr is None
