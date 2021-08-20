class Solution:

    def totalFruit(self, tree):
        ans = cur = one = two = count_one = count_two = 0
        for i in tree:
            if i not in (one, two):
                cur = count_two + 1
            else:
                cur += 1
            if i != two:
                (one, two) = (two, i)
                count_two = 1
            else:
                count_two += 1
            ans = max(ans, cur)
        return ans
