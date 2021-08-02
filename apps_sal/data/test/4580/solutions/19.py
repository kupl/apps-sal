n = int(input())
player = list(map(int, input().split()))
result = [0] * 8
free_color = 0
for i in range(n):
    color = player[i] // 400
    if color < 8:
        result[color] = 1
    else:
        free_color += 1
num = 8 - result.count(0)
print(("{} {}".format(max(num, 1), num + free_color)))
