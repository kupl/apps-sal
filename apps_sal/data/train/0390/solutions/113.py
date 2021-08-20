class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        mem = {}

        def get_dp(i):
            if i == 0:
                return False
            elif i not in mem:
                root = 1
                while True:
                    if root * root > i:
                        mem[i] = False
                        break
                    else:
                        if not get_dp(i - root * root):
                            mem[i] = True
                            break
                        root += 1
            return mem[i]
        return get_dp(n)
