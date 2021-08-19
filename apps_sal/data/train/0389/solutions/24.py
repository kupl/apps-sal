class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        A_sum = float(sum(A))
        max_sublen = len(A) // 2

        targets = {}
        last_valid_target = None
        for i in range(1, max_sublen + 1):
            target = A_sum * i / len(A)
            if target % 1 == 0:
                last_valid_target = int(target)
                targets[last_valid_target] = i

        if last_valid_target is None:
            return False

        dp = [set() for _ in range(last_valid_target + 1)]
        dp[0].add(0)
        for i in range(len(A)):
            for sum_ in range(last_valid_target, A[i] - 1, -1):
                set2 = dp[sum_ - A[i]]
                if A[i] == 0:
                    set2 = dp[sum_ - A[i]].copy()
                for n in set2:
                    dp[sum_].add(n + 1)
                    if sum_ in targets and targets[sum_] == n + 1:
                        # print(dp)
                        #print(sum_, n+1)
                        return True

        return False
