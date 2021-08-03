n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
alist = []
for i in range(m - 1):
    alist.append(x[i + 1] - x[i])
alist.sort()
if n >= m:
    print(0)
else:
    print(sum(alist[0:m - n]))
