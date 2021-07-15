t = int(input())
for i in range(t):
    n = list(input())
    if len(n) == 1:
        print(int(n[0]))
    else:
        count = (len(n) - 1) * 9
        flag = True
        for i in range(len(n) - 1):
            if n[i] < n[i + 1]:
                break
            if n[i] > n[i + 1]:
                flag = False
                break
        if flag:
            count += int(n[0])
        else:
            count += int(n[0]) - 1
        print(count)
