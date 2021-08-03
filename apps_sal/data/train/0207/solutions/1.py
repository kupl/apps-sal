class Solution:
    class MyNumber:
        def __init__(self, v):
            self.str_val = str(v)
            self.val = [int(x) for x in self.str_val]
            self.n = len(self.val)

        def __cmp__(self, other):
            n1 = self.str_val + other.str_val
            n2 = other.str_val + self.str_val
            return 0 if n1 == n2 else 1 if n1 > n2 else -1

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if all(x == 0 for x in nums):
            return '0'
        myns = [self.MyNumber(x) for x in nums]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if myns[j].__cmp__(myns[i]) > 0:
                    t = myns[i]
                    myns[i] = myns[j]
                    myns[j] = t

        return "".join([x.str_val for x in myns])
