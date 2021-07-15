n, m = list(map(int, input().split()))
x = tuple(map(int, input().split()))
y = min(x)
a = 0
for xi in x:
    b = xi - y
    while b:
        a, b = b, a % b
j = 1
for p in input().split():
    if a % int(p):
        j += 1
        continue
    print("YES")
    print(y, j)
    break
else:
    print("NO")

