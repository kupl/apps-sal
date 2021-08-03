n = 6
m = 8
desk = []
stat = []
stat.append("33-44-33")
stat.append("33-44-33")
stat.append("22-33-22")
stat.append("22-33-22")
stat.append("11-22-11")
stat.append("11-22-11")
for i in range(n):
    desk.append(input())
flag = 0
val = 4
while flag == 0:
    for i in range(n):
        for j in range(m):
            if (desk[i][j] == '.'):
                if (flag == 0 and val == 4 and stat[i][j] == '4'):
                    desk[i] = desk[i][:j] + 'P' + desk[i][j + 1:]
                    flag = 1
                if (flag == 0 and val == 3 and stat[i][j] == '3'):
                    desk[i] = desk[i][:j] + 'P' + desk[i][j + 1:]
                    flag = 1
                if (flag == 0 and val == 2 and stat[i][j] == '2'):
                    desk[i] = desk[i][:j] + 'P' + desk[i][j + 1:]
                    flag = 1
                if (flag == 0 and val == 1 and stat[i][j] == '1'):
                    desk[i] = desk[i][:j] + 'P' + desk[i][j + 1:]
                    flag = 1
    val = val - 1

for i in desk:
    print(i)
