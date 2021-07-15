nrofexams = int(input(''))

exams = []
for i in range(nrofexams):
    line = input('').split()
    tup = (int(line[0]), int(line[1]))
    exams.append(tup)

exams = sorted(exams)
date = 0
for i in range(len(exams)):
    if (date<=exams[0][1]):
        date = exams[0][1]
    else:
        date = exams[0][0]
    exams.pop(0)
print(date)

