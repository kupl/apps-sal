class Solution:
    def isValidSerialization(self, preorder):
        new_preorder = preorder
        for i in range(len(new_preorder) - 1, 0, -1):
            if (new_preorder[i] != '
                preorder=preorder[:i] + preorder[i + 1:]
        print(preorder)
        num=0
        sharp=0
        for i in range(0, len(preorder)):
            print((num, sharp))
            if sharp > num:
                return False
            elif preorder[i] == '
                sharp += 1
                if sharp == num + 1 and num == int(((len(preorder) / 2) + 1) / 2):
                    return True
            elif preorder[i] != ',':
                num += 1

        print((num, sharp))
        if num != sharp - 1:
            return False
        """
         :type preorder: str
         :rtype: bool
         """
