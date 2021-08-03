N, T = list(map(int, input().split()))
t = list(map(int, input().split()))
d = []

for i in range(N - 1):
    tmp = t[i + 1] - t[i]
    if tmp > T:
        d.append(T)
    else:
        d.append(tmp)

print(sum(d) + T)
