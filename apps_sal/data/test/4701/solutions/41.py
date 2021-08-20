import math
ans = 1
count = 0
num1 = int(input())
num2 = int(input())
for i in range(num1):
    if ans < num2:
        ans *= 2
    else:
        ans += num2
print(ans)
