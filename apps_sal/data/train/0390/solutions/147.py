class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        cache = {}

        def helper(number):
            if number == 0:
                return False
            if number not in cache:
                flag = False
                for i in range(1, 317):
                    val = i ** 2
                    if val > number:
                        break
                    if not helper(number - val):
                        flag = True
                        break
                cache[number] = flag
            return cache[number]
        return helper(n)
