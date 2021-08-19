n = int(input())
h = [0] + list(map(int, input().split())) + [0]
cnt = 0
while True:
    zero_ind = []
    for i in range(n + 2):
        if h[i] == 0:
            zero_ind.append(i)
    (start, end) = ([], [])
    for i in range(len(zero_ind) - 1):
        if zero_ind[i + 1] - zero_ind[i] > 1:
            start.append(zero_ind[i] + 1)
            end.append(zero_ind[i + 1])
    for (s, e) in zip(start, end):
        for i in range(s, e):
            h[i] -= 1
        cnt += 1
    if h.count(0) == n + 2:
        break
print(cnt)
