class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        check = []
        for i in range(1,n+1):
            if n % i == 0:
                check.append(i)
        if len(check) < k:
            return -1
        else:
            return check[k-1]
