n, x = map(int, input().split())
l = list(map(int, input().split()))
time = 0
l.sort()
for i in range(n):
    if(x == 1):
        time = time + (x * sum(l[i:n]))
        break
    else:
        temp = l[i]
        time = time + (x * temp)
        x = x - 1
print(time)
