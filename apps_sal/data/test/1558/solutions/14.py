__author__ = 'Ekaterina'
n, r, avg = (int(m) for m in input().split())
exams = []
for i in range(n):
    input_i = [int(m) for m in input().split()]
    exams.append([input_i[1], input_i[0]])
exams.sort()
current_sum = exams[0][1]
works_to_do = 0
for x in range(1, n):
    current_sum += exams[x][1]
needed_points = avg*n - current_sum
if needed_points <= 0:
    print(0)
else:
    j = 0
    while needed_points > 0:
        points_subject = r - exams[j][1]
        if needed_points == points_subject:
            works_to_do = works_to_do + exams[j][0]*points_subject
            break
        elif needed_points < points_subject:
            works_to_do = works_to_do + exams[j][0]*needed_points
            break
        elif needed_points > points_subject:
            needed_points = needed_points - points_subject
            works_to_do = works_to_do + exams[j][0]*points_subject
        j += 1
    print(works_to_do)
