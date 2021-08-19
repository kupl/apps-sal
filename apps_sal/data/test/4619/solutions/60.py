(w, h, n) = list(map(int, input().split()))
s_w = [0, w]
s_h = [0, h]
for _ in range(n):
    (x, y, a) = list(map(int, input().split()))
    if a == 1 and x > s_w[0]:
        s_w[0] = x
    elif a == 2 and x < s_w[1]:
        s_w[1] = x
    elif a == 3 and y > s_h[0]:
        s_h[0] = y
    elif a == 4 and y < s_h[1]:
        s_h[1] = y
ans_w = s_w[1] - s_w[0]
ans_h = s_h[1] - s_h[0]
print(ans_w * (ans_w > 0) * (ans_h * (ans_h > 0)))
