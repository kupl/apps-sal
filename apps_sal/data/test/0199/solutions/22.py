import math
ns = list(map(int, input().rstrip().split()))
n = ns[0]
s = ns[1]
data = list(map(int, input().rstrip().split()))
data.sort()
extras = [i - data[0] for i in data]
total = sum(data)
extratotal = sum(extras)
if s > total:
    print(-1)
elif extratotal >= s:
    print(data[0])
else:
    sub = math.ceil((s - extratotal) / n)
    print(data[0] - sub)
