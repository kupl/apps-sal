'''
ABC052_a A - Two Rectangles
https://atcoder.jp/contests/abc052/tasks/abc052_a
'''

class Solver:
    """ solve ABC052_a class """
    ans = 0

    def __init__(self, a, b, c, d):
        self.solve(a, b, c, d)

    def compare(self, s1, s2):
        return s1 if s1 > s2 else s2

    def calc_area(self, h, w):
        return h*w

    def solve(self, h1, w1, h2, w2):
        s1 = self.calc_area(h1, w1)
        s2 = self.calc_area(h2, w2)
        self.ans = self.compare(s1, s2)

def input_data():
    return list(map(int, input().split()))

def main():
    a, b, c, d = input_data()
    answer = Solver(a, b, c, d).ans
    print(answer)

def __starting_point():
    main()

__starting_point()
