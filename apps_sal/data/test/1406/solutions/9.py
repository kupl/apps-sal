
n, k, d = list(map(int, input().split()))


success = True

answer = [[] for x in range(n)]

answer[0] = [1 for x in range(d)]

for i_th_student in range(1, n):

    i_minus_one_student = answer[i_th_student - 1]

    current_student = list(i_minus_one_student)

    for i_th_day in reversed(list(range(d))):

        if i_minus_one_student[i_th_day] < k:

            current_student[i_th_day] += 1

            for i in range(i_th_day + 1, d):
                current_student[i] = 1

            break

    answer[i_th_student] = current_student

    if current_student == i_minus_one_student:
        success = False
        break

if not(success):
    print("-1")

else:
    answer_trans = [[] for i in range(d)]
    for y in range(n):
        i = 0
        for x in answer[y]:
            answer_trans[i].append(x)
            i += 1
    for bla in answer_trans:
        print(' '.join(map(str, bla)))
