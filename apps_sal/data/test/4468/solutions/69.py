(N, T) = [int(i) for i in input().split(' ')]
t = [int(j) for j in input().split(' ')]
dt = []
for i in range(N - 1):
    dt.append(t[i + 1] - t[i])
else:
    dt.append(T)
print(sum([min([dti, T]) for dti in dt]))
