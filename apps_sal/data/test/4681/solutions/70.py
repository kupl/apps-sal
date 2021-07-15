n = int(input())
data = [0]*87
data[0] = 2
data[1] = 1
if n >= 2:
    for i in range(2,n+1):
        data[i] =data[i-1] + data[i-2]
print(data[n])
