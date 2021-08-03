n, k = map(int, input().split(" "))
a = sorted([list(map(int, input().split(" "))) for i in range(n)])
count = 0
for x, y in a:
    count += y
    if k <= count:
        print(x)
        break
else:
    print("None")
