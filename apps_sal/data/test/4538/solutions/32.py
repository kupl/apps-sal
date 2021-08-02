n, d = list(map(int, input().split()))
count = 0
for i in range(n):
    x, y = list(map(int, input().split()))
    if d**2 >= (x**2 + y**2):
        count += 1
print(count)
