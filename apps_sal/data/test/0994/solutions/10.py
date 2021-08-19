(n, m) = map(int, input().split())
possible = True
(day_prev, h_prev) = map(int, input().split())
h_max = h_prev + (day_prev - 1)
for i in range(m - 1):
    (day, h) = map(int, input().split())
    if abs(h - h_prev) > day - day_prev:
        possible = False
        break
    h_new = max(h, h_prev) + (day - day_prev - abs(h - h_prev)) // 2
    h_max = max(h_max, h_new)
    (day_prev, h_prev) = (day, h)
h_max = max(h_max, h_prev + (n - day_prev))
if possible:
    print(h_max)
else:
    print('IMPOSSIBLE')
