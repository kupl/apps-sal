n = int(input())
a = [list(map(int, input().split())) + [i] for i in range(n)]
b = a.copy()
(max_L_1, max_L_2, min_R_1, min_R_2) = (0, 0, 0, 0)
b.sort(reverse=True)
(max_L_1, max_L_2) = (b[0][2], b[1][2])
b.sort(key=lambda x: x[1])
(min_R_1, min_R_2) = (b[0][2], b[1][2])
max_l = 0
for i in range(n):
    left = a[max_L_1][0] if i != max_L_1 else a[max_L_2][0]
    right = a[min_R_1][1] if i != min_R_1 else a[min_R_2][1]
    max_l = max(right - left, max_l)
print(max_l)
