line = input().split(' ')
n = int(line[0])
r = int(line[1])
avg = int(line[2])


class Exam:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return repr((self.a, self.b))


i = 0
s = 0
lst = []
while i < n:
    line = input().split(' ')
    a = int(line[0])
    b = int(line[1])
    lst.append(Exam(a, b))
    s += a
    i += 1
lst.sort(key=lambda exam: exam.b)
ans = 0
avg *= n
for exam in lst:
    if s >= avg:
        break
    ans += min(r - exam.a, avg - s) * exam.b
    s += min(r - exam.a, avg - s)
print(ans)
