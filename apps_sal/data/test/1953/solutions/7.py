a = int(input())
x = [int(x) for x in input().split()]
x.sort()
time = 0
c = 0
for i in range(a):
    if x[i] >= time:
        time += x[i]
        c += 1
print(c)
