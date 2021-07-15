class Solution:
    def canArrange(self, arr, k):
        rem = [0] * k
        for a in arr:
            rem[a % k] += 1
        if rem[0] % 2 != 0:
            return False
        for i in range(1, (k - 1) // 2 + 1):
            if rem[k - i] != rem[i]:
                return False
        return True  
