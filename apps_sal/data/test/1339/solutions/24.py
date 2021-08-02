n = int(input())

L = []
R = []
pair = []
for i in range(n):
    l, r = input().split()
    L.append(int(l))
    R.append(int(r))
    pair.append(l + '-' + r)

minL = min(L)
maxR = max(R)

if (str(minL) + '-' + str(maxR)) in pair:
    print(pair.index(str(minL) + '-' + str(maxR)) + 1)
else:
    print(-1)
