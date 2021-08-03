n = int(input())
red = [tuple(map(int, input().split())) for _ in range(n)]
blue = [tuple(map(int, input().split())) for _ in range(n)]
red.sort(key=lambda x: -x[1])
blue.sort()
count = 0
for xb, yb in blue:
    for i in range(n):
        if xb > red[i][0] and yb > red[i][1]:
            red[i] = (201, 201)
            count += 1
            break
print(count)
