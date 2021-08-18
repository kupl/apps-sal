def main():
    n = int(input())
    x, y = list(map(int, input().split()))
    a = []
    for i in range(n):
        a.append(input().split())
    for i in range(n):
        a[i][1] = int(a[i][1]) - x
        a[i][2] = int(a[i][2]) - y
    typneedbql = []
    typneedbqr = []
    typneedbqu = []
    typneedbqd = []
    typneedrlu = []
    typneedrru = []
    typneedrld = []
    typneedrrd = []
    for i in range(n):
        if (a[i][1] * a[i][2] == 0 and a[i][1] < 0):
            typneedbql.append([abs(a[i][1] + a[i][2])] + a[i])
        elif (a[i][1] * a[i][2] == 0 and a[i][1] > 0):
            typneedbqr.append([abs(a[i][1] + a[i][2])] + a[i])
        elif (a[i][1] * a[i][2] == 0 and a[i][2] > 0):
            typneedbqu.append([abs(a[i][1] + a[i][2])] + a[i])
        elif (a[i][1] * a[i][2] == 0 and a[i][2] < 0):
            typneedbqd.append([abs(a[i][1] + a[i][2])] + a[i])
        elif (abs(a[i][1] / a[i][2]) == 1 and a[i][1] < 0 and a[i][2] < 0):
            typneedrlu.append([abs(a[i][1])] + a[i])
        elif (abs(a[i][1] / a[i][2]) == 1 and a[i][1] < 0 and a[i][2] > 0):
            typneedrld.append([abs(a[i][1])] + a[i])
        elif (abs(a[i][1] / a[i][2]) == 1 and a[i][1] > 0 and a[i][2] > 0):
            typneedrrd.append([abs(a[i][1])] + a[i])
        elif (abs(a[i][1] / a[i][2]) == 1 and a[i][1] > 0 and a[i][2] < 0):
            typneedrru.append([abs(a[i][1])] + a[i])
    typneedbql.sort()
    typneedbqr.sort()
    typneedbqd.sort()
    typneedbqu.sort()
    typneedrlu.sort()
    typneedrru.sort()
    typneedrld.sort()
    typneedrrd.sort()
    for i in range(len(typneedbql)):
        if typneedbql[i][1] == "R" or typneedbql[i][1] == "Q":
            print("YES")
            return
        else:
            break
    for i in range(len(typneedbqr)):
        if typneedbqr[i][1] == "R" or typneedbqr[i][1] == "Q":
            print("YES")
            return
        else:
            break
    for i in range(len(typneedbqu)):
        if typneedbqu[i][1] == "R" or typneedbqu[i][1] == "Q":
            print("YES")
            return
        else:
            break
    for i in range(len(typneedbqd)):
        if typneedbqd[i][1] == "R" or typneedbqd[i][1] == "Q":
            print("YES")
            return
        else:
            break
    for i in range(len(typneedrlu)):
        if typneedrlu[i][1] == "B" or typneedrlu[i][1] == "Q":
            print("YES")
            return
        else:
            break
    for i in range(len(typneedrld)):
        if typneedrld[i][1] == "B" or typneedrld[i][1] == "Q":
            print("YES")
            return
        else:
            break
    for i in range(len(typneedrrd)):
        if typneedrrd[i][1] == "B" or typneedrrd[i][1] == "Q":
            print("YES")
            return
        else:
            break
    for i in range(len(typneedrru)):
        if typneedrru[i][1] == "B" or typneedrru[i][1] == "Q":
            print("YES")
            return
        else:
            break
    print("NO")


main()
