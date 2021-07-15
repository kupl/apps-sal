class Solution:
    def minOperations(self, n: int) -> int:
        even = n % 2 == 0 and True or False
        half = even and int(n/2) or n//2
        left = right = 0
        for i in range(n):
            if i < half:
                left += (2*i)+1
            elif i == half and even:
                return left
            elif i > half:
                right += (2*i)+1
    
        return int((right - left) / 2)
