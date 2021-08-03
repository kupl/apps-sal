n = int(input())
ai = list(map(int, input().split()))
num = 0
num2 = 0
for i in range(n):
    if ai[i] > 0:
        num += 1
    elif ai[i] < 0:
        num2 += 1
n2 = n // 2 + n % 2
if num >= n2:
    print(1)
elif num2 >= n2:
    print(-1)
else:
    print(0)
