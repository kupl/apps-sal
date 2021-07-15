input()
a = list(map(int, input().split()))
a.sort(reverse=True)
x = a[0]
y1 = x + 1
for y in a:
    if x % y or y == y1:
        print(x, y)
        break
    y1 = y

