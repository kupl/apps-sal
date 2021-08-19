class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = list(map(int, list(str(n))))
        last = None
        for i in range(0, len(digits) - 1):
            if digits[i + 1] > digits[i]:
                last = i

        if last == None:
            return -1
        rst = ""
        i = last
        for j in range(0, i):
            rst += str(digits[j])
            # print(rst)
        p = digits[i]
        for x in range(p + 1, 10):
            if x in digits[i + 1::]:
                break
        rst += str(x)
        # print(rst)
        used = False
        for p in sorted([digits[i]] + digits[i + 1::]):
            if p == x and not used:
                used = True
            else:
                rst += str(p)
            # print(rst)
        f = int(rst)
        if f > 2147483647:
            return -1
        else:
            return f
