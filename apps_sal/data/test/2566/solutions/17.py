import sys
n = int(sys.stdin.readline())
for i in range(n):
    lessons = int(sys.stdin.readline())
    tmpSchedule = str(sys.stdin.readline()).split()
    ans = -1
    for j in range(7):
        schedule = [tmpSchedule[k % 7] for k in range(j, j + 7)]
        worked = []
        for i in range(len(schedule)):
            if schedule[i] == '1':
                worked.append(i + 1)
        atWeek = schedule.count('1')
        tmpAns = (lessons - 1) // atWeek * 7
        tmp = lessons % atWeek - 1
        if tmp < 0:
            tmp = len(worked) - 1
        tmpAns += worked[tmp] - worked[0] + 1
        if tmpAns < ans or ans == -1:
            ans = tmpAns
    print(ans)
