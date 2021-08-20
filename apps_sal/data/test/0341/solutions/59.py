(N, K) = [int(x) for x in input().split()]
(R, S, P) = [int(x) for x in input().split()]
T = input()
point = {'r': P, 's': R, 'p': S}
win = [False] * N
total = 0
for i in range(N):
    if i < K or T[i] != T[i - K] or win[i - K] == False:
        total += point[T[i]]
        win[i] = True
print(total)
