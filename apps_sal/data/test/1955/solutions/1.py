D = input().split()
D = [int(x) for x in D]
n = D[0]
m = D[1]
d = input().split()
d = [int(x) for x in d]
A = [int(x) for x in input().split()]
S = 0
so = 0
neg = 0
ind = 0
days = 0
for i in d:
    if i == 0:
        neg += 1
for i in A:
    so += i
if so + m > n or n - neg < m:
    print(-1)
else:
    p = A.pop(0)
    for i in d:
        if i > 0 and ind > 0 and (p != 0):
            ind -= 1
            days += 1
        elif i > 0 and ind > 0:
            ind -= 1
            days += 1
            if ind == 0:
                break
            else:
                for j in range(days, n):
                    days += 1
                    if d[j] > 0:
                        ind -= 1
                        if ind == 0:
                            break
                break
        else:
            S += 1
            days += 1
        if p == S and A != []:
            ind += 1
            S = 0
            p = A.pop(0)
        elif p == S:
            ind += 1
            S = 0
            p = 0
    print(days)
