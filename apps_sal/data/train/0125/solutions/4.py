class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        temp1 = a
        temp = 1
        for i in range(len(b) - 1, -1, -1):
            if i < len(b) - 1:
                temp1 = pow(temp1, 10) % 1337
            temp2 = pow(temp1, b[i]) % 1337
            temp = temp * temp2 % 1337
        return temp
