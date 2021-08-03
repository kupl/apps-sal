class Solution(object):
    def minSteps(self, n):
        steps = 0
        div = 2
        while n > 1:
            if n % div == 0:
                steps += div

                n = n / div
            else:
                div += 1

        return steps
