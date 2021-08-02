class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.mem = {}

        return self.top_down(n)

    def merge(self, left, right):
        comb = []
        for i in left:
            comb += [i + j for j in right]

        return list(set(comb))

    def top_down(self, n):
        if n == 1:
            return ['()']

        if not n - 1 in self.mem:
            self.mem[n - 1] = self.top_down(n - 1)
        rest = self.mem[n - 1]
        comb = ['(' + i + ')' for i in rest]

        for i in range(1, n):

            if not i in self.mem:
                self.mem[i] = self.top_down(i)
            comb_left = self.mem[i]
            if not n - i in self.mem:
                self.mem[n - i] = self.top_down(n - i)
            comb_right = self.mem[n - i]

            comb += self.merge(comb_left, comb_right)

        comb = list(set(comb))

        return comb
