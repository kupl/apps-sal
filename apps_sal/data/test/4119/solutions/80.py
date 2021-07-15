n, m = list(map(int, input().split()))
x = sorted(list(map(int, input().split())))
y = []
if n > m :
    print((0))
    return
for i in range(m-1):
    diff = x[i+1] - x[i]
    y.append(diff)
y.sort(reverse = True)
res = x[-1] - x[0]
for i in range(n-1):
    res -= y[i]
print(res)

