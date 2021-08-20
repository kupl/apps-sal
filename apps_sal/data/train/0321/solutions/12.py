class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        arr1 = list(s1)
        arr2 = list(s2)
        arr1.sort()
        arr2.sort()
        c = 0
        for i in range(len(arr1)):
            if arr1[i] > arr2[i]:
                break
            c += 1
        if c == len(arr1):
            return True
        for i in range(len(arr1)):
            if arr1[i] < arr2[i]:
                return False
            c += 1
        return True
