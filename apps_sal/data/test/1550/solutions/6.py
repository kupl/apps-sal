n = int(input())
num = input()
status = 0
check = num[0]
for i in num:
    if i != check:
        status = 1
        break
if status == 0:
    for i in range(n):
        print(0,end="")
    print()
else:
    maximum = 0
    consider = []
    for i in range(10):
        dum = ""
        for j in range(n):
            dum = dum + (str(((int(num[j]) + i) % 10)))
        count = 0
        cur = 0
        ind = []
        for j in range(n):
            if dum[j] != '0':
                if cur > count:
                    count = cur
                    ind = [j-count]
                elif cur == count:
                    ind.append(j-count)
                cur = 0
            else:
                cur += 1
        if cur != 0:
            if cur > count:
                count = cur
                ind = [j-count+1]
            elif cur == count:
                ind.append(j-count+1)
        if count > maximum:
            consider = []
            for i in ind:
                consider.append([dum,i])
                maximum = count
        elif count == maximum:
            for i in ind:
                consider.append([dum,i])
    out = []

    for i in range(len(consider)):
        out.append(consider[i][0][consider[i][1]:] + consider[i][0][:consider[i][1]])
    print(min(out))

