s = int(input())


class Solution:
    def __init__(self, s):
        self.s = s

    def function_a(self):
        if self.s % 2 == 0:
            return self.s / 2
        else:
            return 3 * self.s + 1

    def answer(self):
        list_a = [self.s]
        self.s = self.function_a()
        ans = 2
        while self.s not in list_a:
            list_a.append(self.s)
            self.s = self.function_a()
            ans += 1
        print(ans)


conditon = Solution(s)
conditon.answer()
