n = int(input())
for i in range(n):
    s, t = list(map(str, input().split()))
    if len(s) == 1:
        if s < t:
            print(s)
        else:
            print("---")
        continue
    mas = [['ZZ', -1]]
    for j in range(len(s) - 1, -1, -1):
        if mas[-1][0] > s[j]:
            mas.append([s[j], j])
        else:
            mas.append(mas[-1])
    mas = mas[::-1]
    #print (*mas)
    flag = True
    for j in range(len(s)):
        #print (j)
        if s[j] > mas[j][0]:
            s = s[:j] + mas[j][0] + s[j + 1:mas[j][1]] + s[j] + s[mas[j][1] + 1:]
            if (s >= t):
                print("---")
            else:
                print(s)
            flag = False
            break
    if flag:
        if s < t:
            print(s)
        else:
            print("---")
