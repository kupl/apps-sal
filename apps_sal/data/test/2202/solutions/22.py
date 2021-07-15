np = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

max = 0

mod = []
sum = 0
for i in range(0, np[0]) :
    sum += a[i]
    mod.append(sum % np[1])
index = 0
mm = 0
for i in range(0, np[0]) :
    if mod[i] > mm :
        mm = mod[i]
        index = i


sum2 = 0;
for i in range(index+1, np[0]) :
    sum2 += a[i]
sum2 = sum2 % np[1]

print(mod[index] + sum2)


