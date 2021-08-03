class Solution:
    def ones_gen(self):
        ones = 1

        while True:
            yield ones
            ones = ones * 10 + 1

    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        for o in self.ones_gen():
            if o % k == 0:
                return len(str(o))
