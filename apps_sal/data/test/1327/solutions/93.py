n, m = [int(s) for s in input().split()]
cake_list = [[int(s) for s in input().split()] for _ in range(n)]

ans_list = [0] * 8
for i in range(8):
    a, b, c = [1 if (i >> j) & 1 == 1 else -1 for j in range(3)]
    temp_list = sorted([a * x + b * y + c * z for x, y, z in cake_list], reverse=True)

    for j in range(m):
        ans_list[i] += temp_list[j]
print(max(ans_list))
