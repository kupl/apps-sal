lst = list(map(int, input().split()))
n = lst[0]
b = list(map(int, input().split()))
max = -1
min = 10000000000
maxf = 0
minf = 0
for x in b:
    if(x > max):
        maxf = 1
        max = x
    elif x == max:
        maxf += 1
    if(x < min):
        minf = 1
        min = x
    elif x == min:
        minf += 1
if(max == min):
    print(max - min, maxf * (maxf - 1) // 2)
else:
    print(max - min, maxf * minf)
