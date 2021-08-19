class Solution:

    def recursion(self, arr, index, s):
        if (index < 0) | (index >= len(arr)):
            return False
        elif arr[index] == 0:
            return True
        elif index in s:
            return False
        else:
            s.add(index)
            return self.recursion(arr, index + arr[index], s) | self.recursion(arr, index - arr[index], s)

    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 not in arr:
            return False
        s = set()
        return self.recursion(arr, start, s)
