import bisect
n = int(input())
a = [int(x) for x in input().split()]
a = sorted(a)
p2 = []
for i in range(1, 31):
    p2.append(2 ** i)
c = 0
if n == 1:
    print(1)
else:
    for i in range(0, n):
        flag = 0
        for j in p2:
            if j > a[i]:
                d = j - a[i]
                f = bisect.bisect(a, d)
                if d != a[i]:
                    if a[f - 1] == d:
                        flag = 100
                        break
                elif i != f - 1:
                    if a[f - 1] == d:
                        flag = 100
                        break
                elif a[f - 2] == d:
                    flag = 100
                    break
        if flag == 0:
            c = c + 1
    print(c)
