n = int(input())
k = int(input())
x = 1
for i in range(n):
    if x + k <= 2 * x:
        x += k
    else:
        x *= 2
print(x)
