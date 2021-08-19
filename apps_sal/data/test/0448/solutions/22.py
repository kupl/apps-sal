data = input().split()
n = int(data[0])
k = int(data[1])
data = input().split()
for i in range(len(data)):
    data[i] = int(data[i])
ans = 0
last = (data[0] - 1) // k
for i in range(1, len(data)):
    if (data[i] - 1) // k >= last:
        ans = i
        last = (data[i] - 1) // k
print(ans + 1)
