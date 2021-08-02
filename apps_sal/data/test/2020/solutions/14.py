n = int(input())

x_set = set()
y_set = set()

for i in range(n):
    x, y = map(int, input().split())

    x_set.add(x)
    y_set.add(y)

print(min(len(x_set), len(y_set)))
