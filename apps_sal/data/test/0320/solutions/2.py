n = int(input())
a = 0
b = 0
ans = 0
for i in range(n):
    (x, y) = list(map(int, input().split()))
    if (x + y) % 2 == 1:
        ans = 1
    a += x
    b += y
if (a + b) % 2 == 1:
    print(-1)
elif a % 2 == b % 2 == 0:
    print(0)
elif ans == 0:
    print(-1)
else:
    print(1)
