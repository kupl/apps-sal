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
        finish = False

        for i in range(1, len(preorder)):
            if not curr:
                return False

            e = preorder[i]

            if e != '
            s.append((curr, on_left))
            curr = e
            on_left = True
            finish = False
            else:
                if not on_left:
                    curr = None
                    finish = True

                    while len(s) and not on_left:
                        curr, on_left = s.pop()

                    if curr and not on_left:
                        curr = None

                on_left = False

        return finish
