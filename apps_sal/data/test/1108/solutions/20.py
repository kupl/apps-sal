n = int(input())
k = 0
for i in range(n):
    (x, y) = [int(x) for x in input().split()]
    if y - x >= 2:
        k += 1
print(k)
