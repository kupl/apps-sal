n = int(input())
a, b = list(map(int, input().split())), list(map(int, input().split()))
r = 0
for i in range(n):
    if 2 * a[i] >= b[i] and b[i] > 1:
        x = b[i] // 2
        y = b[i] - x
        r += x * y
    else:
        r -= 1
print(r)
