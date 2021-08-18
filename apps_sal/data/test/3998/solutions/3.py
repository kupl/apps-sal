n = (int(input()))
R = list(map(int, input().split()))
Time = 0
check = False
Output = []
while (check == False):
    pos_max = []
    pos_sec = []
    Max_sec = -1
    Max_num = 0
    Max = -1
    Min = 999999999
    Time += 1
    string = ''
    for i in range(len(R) - 1, -1, -1):
        if (R[i] < Min):
            Min = R[i]
        if (R[i] > Max):
            Max_sec = Max
            Max = R[i]
            pos_sec = pos_max
            pos_max = []
            pos_max.append(i)
            Max_num = 1
        elif (R[i] == Max):
            Max_num += 1
            pos_max.append(i)
        elif (R[i] > Max_sec):
            Max_sec = R[i]
            pos_sec = []
            pos_sec.append(i)
    if (Max == Min):
        check = True
        break
    if (Max_num > 1):
        if (Max_num % 2 == 1):
            j = 0
            some = []
            for k in range(n - 1, -1, -1):
                if (pos_max[j] == k):
                    if (R[k] != 0):
                        R[k] -= 1
                    some.append(k)
                    j += 1
                    if (j > 2):
                        j = 0
            j = len(some) - 1
            for k in range(n):
                if (some[j] == k):
                    string += '1'
                    j -= 1
                    if (j < 0):
                        j = 0
                else:
                    string += '0'
        else:
            j = 0
            some = []
            for k in range(n - 1, -1, -1):
                if (pos_max[j] == k):
                    if (R[k] != 0):
                        R[k] -= 1
                    some.append(k)
                    j += 1
                    if (j > 1):
                        j = 1
            j = len(some) - 1
            for k in range(n):
                if (some[j] == k):
                    string += '1'
                    j -= 1
                    if (j < 0):
                        j = 0
                else:
                    string += '0'
    else:
        for k in range(n):
            if (pos_max[0] == k):
                if (R[k] != 0):
                    R[k] -= 1
                string += '1'
                continue
            if (pos_sec[0] == k):
                if (R[k] != 0):
                    R[k] -= 1
                string += '1'
                continue
            string += '0'
    Output.append(string)

print(Max)
print(Time - 1)
for i in range(len(Output)):
    print(Output[i])
