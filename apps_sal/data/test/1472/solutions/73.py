(N, X, Y) = list(map(int, input().split()))
dict_lis = {i: 0 for i in range(1, N)}
for i in range(1, N):
    for j in range(i + 1, N + 1):
        length_ij = min(j - i, abs(j - Y) + abs(i - X) + 1)
        dict_lis[length_ij] += 1
for i in range(1, N):
    print(dict_lis[i])
