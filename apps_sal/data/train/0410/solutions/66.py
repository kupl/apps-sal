class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        int_to_steps = {}
        for x in range(lo, hi + 1):
            start = x
            steps = 0
            while x != 1:
                steps += 1
                if x % 2 == 0:
                    x = x / 2
                else:
                    x = x * 3 + 1
            int_to_steps[start] = steps

        return sorted(list(int_to_steps.items()), key=lambda item: item[1])[k - 1][0]
