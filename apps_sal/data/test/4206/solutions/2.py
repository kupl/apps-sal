n = list(input())
cntr = 0
marks = []
for i in range(len(n)):
    marks.append(0)
for i in range(len(n)):
    if int(n[i]) % 3 == 0:
        #print(i, cntr, marks)
        cntr += 1
        marks[i] = 1
    elif marks[i] == 0:
        marks[i] = 1
        tmpcnt = int(n[i])
        mrk = -1
        for j in range(2):
            if i + j + 1 < len(n):
                if (int(n[i+j+1])% 3 != 0):
                    if (tmpcnt + int(n[i+j+1]) )%3 == 0:
                        cntr += 1
                        mrk = i+j+1
                       # print(i, cntr, marks)
                        break
                    else:
                        tmpcnt += int(n[i+j+1])
                else:
                    break
        if mrk != -1:
            for k in range(i + 1, mrk + 1):
          #      print(i,k)
                marks[k] = 1
print(cntr)

