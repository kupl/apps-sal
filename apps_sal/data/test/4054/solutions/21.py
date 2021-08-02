ingrd = [1, 1, 2, 7, 4]
qunty = list(map(int, input().split()))
mins = []
for i, v in enumerate(qunty):
    mins.append(v // ingrd[i])
print(min(mins))
