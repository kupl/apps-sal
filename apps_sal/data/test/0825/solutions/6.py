n = int(input())
temp = []
for i in range(2, int(n ** 0.5) + 2):
    if n % i == 0:
        temp.append([i, 0])
        while(n % i == 0):
            n /= i
            temp[-1][1] += 1
else:
    if n != 1:
        temp.append([n, 1])
ans = 0
for i in range(len(temp)):
    count = 1
    while(temp[i][1] >= count):
        ans += 1
        temp[i][1] -= count
        count += 1
if len(temp) == 0:
    print((0))
else:
    print(ans)
