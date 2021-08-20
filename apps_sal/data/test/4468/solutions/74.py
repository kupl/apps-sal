(N, T) = list(map(int, input().split()))
t = list(map(int, input().split()))
time = T
for i in range(N - 1):
    if t[i + 1] - t[i] >= T:
        time += T
    else:
        time += t[i + 1] - t[i]
print(time)
