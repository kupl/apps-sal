n = int(input())
cnt = 1
x, y, a, b = 0,0,0,0
for i in range(n):
    x, y = input()
    if i == 0:
        a, b = x, y
    else:
        if a != x:
            cnt += 1
        a, b = x, y
print(cnt)
