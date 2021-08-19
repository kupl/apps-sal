class Solution:
    def maxSum(self, l1: List[int], l2: List[int]) -> int:
        last_p1 = 0
        last_p2 = 0
        p1 = 0
        p2 = 0
        sum_so_far = 0
        while (p1 < len(l1) and p2 < len(l2) and last_p1 < len(l1) and last_p2 < len(l2)):
            if l1[p1] < l2[p2]:
                p1 += 1
            elif l1[p1] > l2[p2]:
                p2 += 1
            else:  # ==
                sum_so_far += max(sum(l1[last_p1:p1]), sum(l2[last_p2:p2]))
                sum_so_far += l1[p1]
                last_p1 = p1 + 1
                last_p2 = p2 + 1
                p1 += 1
                p2 += 1

        if l1[-1] != l2[-1]:
            sum_so_far += max(sum(l1[last_p1:]), sum(l2[last_p2:]))
        return sum_so_far % 1000000007
