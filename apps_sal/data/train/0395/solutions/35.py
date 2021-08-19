class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        from sortedcontainers import SortedSet
        li = A
        dp = SortedSet()  # Ele: tuple(Odd Jump can take to end, Even Jump take to goal)
        res = 1
        answers = dict()
        dp.add(li[-1])
        answers[li[-1]] = (True, True)
        for i in range(len(li) - 2, -1, -1):
            #print(dp, li[i])
            temp = dp.bisect_right((li[i] - 1))
            # print(temp)
            odd_jump = answers[dp[temp]][1] if -1 < temp < len(dp) and dp[temp] >= li[i] else False
            temp = dp.bisect_right((li[i])) - 1
            # print(temp)
            even_jump = answers[dp[temp]][0] if -1 < temp < len(dp) and dp[temp] <= li[i] else False
            dp.add((li[i]))
            answers[li[i]] = (odd_jump, even_jump)
            if odd_jump:
                res += 1
        return res
