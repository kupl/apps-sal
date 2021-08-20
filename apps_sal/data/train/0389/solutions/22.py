class Solution:

    def dp(self, A, index, sum_, size, aux, dp):
        if index == len(A):
            return False
        if size == 0:
            return sum_ == 0
        key = str(index) + str(sum_) + str(size)
        if key in dp:
            return dp[key]
        if A[index] <= sum_:
            aux.append(A[index])
            if self.dp(A, index + 1, sum_ - A[index], size - 1, aux, dp):
                dp[key] = True
                return dp[key]
            aux.pop()
        if self.dp(A, index + 1, sum_, size, aux, dp):
            dp[key] = True
            return dp[key]
        dp[key] = False
        return dp[key]

    def splitArraySameAverage(self, A: List[int]) -> bool:
        n = len(A)
        sum_ = sum(A)
        dp = {}
        ans = []
        tmp1 = A
        for i in range(1, n):
            if sum_ * i % n == 0:
                s1 = sum_ * i
                s1 //= n
                aux = []
                if self.dp(A, 0, s1, i, aux, dp):
                    return True
        return False
