n, m = map(int, input().split())
answers = []
for _ in range(m):
    num, res = input().split()
    num = int(num)
    answers.append([num, res])

AC_cnt = 0
WA_cnt = 0

AC_problems = [0] * n
WA_problems = [0] * n
for answer in answers:
    if answer[1] == 'WA' and AC_problems[answer[0] - 1] != 1:
        WA_problems[answer[0] - 1] += 1
    else:
        if AC_problems[answer[0] - 1] == 0:
            AC_problems[answer[0] - 1] += 1
        else:
            continue
for i in range(len(AC_problems)):
    AC_cnt += AC_problems[i]
    if AC_problems[i] == 1:
        WA_cnt += WA_problems[i]

print(AC_cnt, WA_cnt)
