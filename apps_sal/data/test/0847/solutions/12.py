line = input().split(' ')
n = int(line[0])
x = float(line[1])
num = input().split(' ')
sum = 0
i = 0
while i < n:
    sum += int(num[i])
    i += 1
ans = abs(float(sum)) // x
if abs(float(sum)) / x > ans:
    print(int(ans + 1))
else:
    print(int(ans))
