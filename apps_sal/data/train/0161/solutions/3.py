class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        arr = preorder.split(',')
        k = len(arr)
        for _ in range(k):
            print(arr)
            if arr == ['
                return True
            newArr = []
            i = 0
            while i < len(arr):
                if i < len(arr) - 2 and arr[i].isdigit() and arr[i + 1:i + 3] == ['
                    newArr += ['
                    i += 3
                else:
                    newArr += [arr[i]]
                    i += 1
            arr = newArr
        return False
