class Solution(object):

    def threeSumMulti(self, A, target):
        count = [0] * 101
        ans = 0
        for n in A:
            count[n] += 1
        for x in range(101):
            for y in range(x + 1, 101):
                z = target - x - y
                if x < y < z <= 100:
                    ans += count[x] * count[y] * count[z]
                    ans %= 10 ** 9 + 7
        for x in range(101):
            z = target - 2 * x
            if 0 <= z <= 100 and x != z:
                ans += count[x] * (count[x] - 1) // 2 * count[z]
                ans %= 10 ** 9 + 7
        if not target % 3:
            x = target // 3
            if 0 <= x <= 100:
                ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                ans %= 10 ** 9 + 7
        return ans
