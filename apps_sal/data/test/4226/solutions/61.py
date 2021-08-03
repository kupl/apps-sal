X, Y = list(map(int, input().split()))

cnt = 0

for x in range(X + 1):
    if 2 * x == 4 * X - Y:
        cnt += 1

if cnt == 0:
    print("No")
else:
    print("Yes")
