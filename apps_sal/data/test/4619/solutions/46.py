w, h, n = list(map(int, input().split()))
plots = [list(map(int, input().split())) for _ in range(n)]

w_min, w_max, h_min, h_max = 0, w, 0, h

for i in range(n):
    if plots[i][2] == 1:
        w_min = max(w_min, plots[i][0])
    elif plots[i][2] == 2:
        w_max = min(w_max, plots[i][0])
    elif plots[i][2] == 3:
        h_min = max(h_min, plots[i][1])
    else:
        h_max = min(h_max, plots[i][1])

print((max(0, (w_max - w_min)) * max(0, (h_max - h_min))))

