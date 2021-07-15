def readln(): return list(map(int, input().rstrip().split()))


n = int(input())
data = []
for i in range(0, n):
    data.append(input())

x = data[0]
data = list([a for a in data if a != x])
cx = n - len(data)

if len(data) == 0:
    print("NO")
    return

y = data[0]
data = list([a for a in data if a != y])
cy = n - cx - len(data)

if cx != cy or len(data) != 0:
    print("NO")
else:
    print("YES")
    print("{} {}".format(x, y))

