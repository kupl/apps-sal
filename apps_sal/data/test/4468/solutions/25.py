n, t = map(int, input().split())
time = [int(i) for i in input().split()]
sum = 0
for i in range(len(time)-1):
    if (time[i+1]-time[i]) < t:
        sum += (time[i+1]-time[i])
    else:
        sum += t
print(sum+t)
