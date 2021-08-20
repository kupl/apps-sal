import operator
(n, r, avg) = list(map(int, input().split()))
Goal = n * avg
(Sum, ans) = (0, 0)
Exam = []
for i in range(n):
    (a, b) = list(map(int, input().split()))
    Sum += a
    Exam.append([a, b])
Exam.sort(key=operator.itemgetter(1))
i = 0
while Sum < Goal and i < n:
    d = min(Goal - Sum, r - Exam[i][0])
    ans += d * Exam[i][1]
    Sum += d
    i = i + 1
print(ans)
