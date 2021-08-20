(M, N) = map(int, input().split())
times = []
for m in range(M):
    times.append(list(map(int, input().split())))
man = [0] * N
time = 0
for m in range(M):
    for n in range(N):
        if n == 0:
            time = man[n] + times[m][n]
        else:
            time = max(time, man[n]) + times[m][n]
        man[n] = time
    print(time, end=' ')
print()
