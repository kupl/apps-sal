data = input().split()
n = int(data[0])
k = int(data[1])
data = list(map(int, input().split()))
ans = 0
last = (data[0] - 1) // k
for i in range(1, len(data)):
    if (data[i] - 1) // k >= last:
        ans = i
        last = (data[i] - 1) // k
print(ans + 1)
