n = int(input())
time = list(map(int, input().split()))
t = int(input())
num = []
time.sort()
tmax = time[-1]
tmin = time[0]
if time[-1] - time[0] <= t:
    print(n)
else:
    la = 0
    stu = 0
    for i in range(n):
        if time[i] <= tmin + t:
            stu += 1
            la = i
        else:
            break
    num.append(stu)
    for i in range(1, n):
        if time[i] + t > tmax:
            break
        if time[i] == time[i - 1]:
            stu -= 1
        else:
            x = time[i] + t
            stu -= 1
            if x <= time[la]:
                break
            else:
                for j in range(la + 1, n):
                    if time[j] <= x:
                        stu += 1
                        la = j
            num.append(stu)
    print(max(num))
