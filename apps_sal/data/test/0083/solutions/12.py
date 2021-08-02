n = int(input())
li = list(map(int, input().split()))
plus = 0
minus = 0
for i in li:
    if i > 0:
        plus += 1
    if i < 0:
        minus += 1
if plus >= (n + 1) // 2:
    print(1)
elif minus >= (n + 1) // 2:
    print(-1)
else:
    print(0)
