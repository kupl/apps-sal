data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))
k = 0
o = 0
h = 0
for i in range(data1[0]):
    k += data2[i]
    if k >= o:
        o = k
    if k < h:
        h = k
ans = data1[1] - (o + abs(h)) + 1
if ans > 0:
    print(ans)
else:
    print(0)
