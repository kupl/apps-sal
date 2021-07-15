n = int(input())
a = list(map(int, input().split()))
m = min(a)
M = max(a)
count = 0
for el in a:
    if el != m and el != M:
        count += 1
print(count)

