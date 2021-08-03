n = int(input())
x = 0
for i in range(1, n + 1):
    if i % 64 == 0 and 64 > x:
        ans = i
        x = 64
    elif i % 32 == 0 and 32 > x:
        ans = i
        x = 32
    elif i % 16 == 0 and 16 > x:
        ans = i
        x = 16
    elif i % 8 == 0 and 8 > x:
        ans = i
        x = 8
    elif i % 4 == 0 and 4 > x:
        ans = i
        x = 4
    elif i % 2 == 0 and 2 > x:
        ans = i
        x = 2
    elif i == 1:
        ans = 1
        x = 1
print(ans)
