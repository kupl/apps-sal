(r, d) = list(map(int, input().split()))
count = 0
for i in range(int(input())):
    (x, y, r1) = list(map(int, input().split()))
    k = (x * x + y * y) ** 0.5
    if k - r1 >= r - d and k + r1 <= r:
        count += 1
print(count)
