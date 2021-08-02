N, C = map(int, input().split())
sch = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
rec = [[0, 0] for _ in range(C + 1)]
num_rec = 1

for i in range(N):
    s, t, c = sch[i]
    start = False
    for j in range(1, num_rec + 1):
        if rec[j][0] - int(rec[j][1] == c) < s:
            rec[j] = [t, c]
            start = True
            break
    if not start:
        num_rec += 1
        rec[num_rec] = [t, c]

print(num_rec)
