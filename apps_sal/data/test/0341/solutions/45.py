(N, K) = map(int, input().split())
(S, P, R) = map(int, input().split())
point = {'s': S, 'p': P, 'r': R}
T = str(input())
max_point = 0
for i in range(K):
    while i < N:
        if i + K < N and T[i] == T[i + K]:
            max_point += point[T[i]]
            i = i + 2 * K
        else:
            max_point += point[T[i]]
            i = i + K
print(max_point)
