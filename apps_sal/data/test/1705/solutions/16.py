n = int(input())
lst = list(map(int, input().split()))
x = 0
y = 0
for i in range(n):
    if lst[i] == 1:
        x+=1
    else:
        y += 1
for i in range(n):
    if lst[i] == 1:
        x -= 1
    else:
        y -= 1
    if x == 0 or y == 0:
        print(i + 1)
        return
