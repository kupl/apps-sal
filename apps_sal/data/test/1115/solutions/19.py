i = int(input())
x = [int(i) for i in input().split()]
total_time = 0
for p in x:
    total_time += p
z = int(input())
flag = 0
for mrinal in range(z):
    (a, b) = map(int, input().split())
    if a <= total_time and b >= total_time:
        flag = total_time
        break
    elif total_time < a:
        flag = a
        break
if flag != 0:
    print(flag)
else:
    print(-1)
