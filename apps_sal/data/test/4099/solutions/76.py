N, K, M, = map(int, input().split())
S = map(int, input().split())
total_score = sum(S)


class Achieve:
    def __init__(self, subjects, points, goal):
        self.subjects = subjects
        self.points = points
        self.goal = goal

    def calculation(self):
        ans = self.subjects * self.goal - total_score
        if ans > self.points:
            return ("-1")
        if ans < 0:
            return (0)
        else:
            return (ans)


takahasi = Achieve(N, K, M)
print(takahasi.calculation())
