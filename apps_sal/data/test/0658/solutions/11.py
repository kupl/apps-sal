(n, w, v, u) = map(int, input().split())
max_t_w = 0
flag = True
for i in range(n):
    (x, y) = map(int, input().split())
    max_t_w = max(max_t_w, x / v - y / u)
    if x / v < y / u:
        flag = False
if flag:
    max_t_w = 0
print(w / u + max_t_w)
