n = int(input())
x = 0

for i in range(n):
    if input().count('+') > 0:
        x += 1
    else:
        x -= 1

print(x)
