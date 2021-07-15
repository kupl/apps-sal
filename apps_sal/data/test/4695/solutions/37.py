a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]
x, y = map(int, input().split())
if a.count(x) * a.count(y) > 0 or b.count(x) * b.count(y) > 0 or c.count(x) * c.count(y) > 0:
    print("Yes")
else:
    print("No")
