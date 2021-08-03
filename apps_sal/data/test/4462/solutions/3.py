n = int(input())
a = list(map(int, input().split()))
s = 0
t = 0
u = 0
for i in range(n):
    if a[i] % 4 == 0:
        s = s + 1
    elif a[i] % 2 == 0:
        t = t + 1
    else:
        u = u + 1
if t >= 1:
    if s >= u:
        print("Yes")
    else:
        print("No")
else:
    if s - u >= -1:
        print("Yes")
    else:
        print("No")
