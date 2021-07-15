from collections import namedtuple

Exam = namedtuple("Exam", "id s d c")


def get_exam(day, exams, prepared):
    result = None

    for exam in exams:
        if exam.s <= day and prepared[exam.id] < exam.c and (result is None or exam.d < result.d):
            result = exam

    return result


n, m = list(map(int, input().split()))
exams = []
prepared = [0] * (m + 1)
schedule = [0] * (n + 1)

for i in range(m):
    s, d, c = list(map(int, input().split()))
    exams.append(Exam(i + 1, s, d, c))
    schedule[d] = -1

for day in range(1, n + 1):
    if schedule[day] == -1:
        print(-1)
        return

    if schedule[day] == m + 1:
        continue

    exam = get_exam(day, exams, prepared)

    if exam is None:
        continue

    prepared[exam.id] += 1
    schedule[day] = exam.id

    if prepared[exam.id] == exam.c:
        schedule[exam.d] = m + 1

print(' '.join(map(str, schedule[1:])))

