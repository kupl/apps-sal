K, N = list(map(int, input().split()))
A_list = list(map(int, input().split()))
A_list.append(K + A_list[0])

dif_list = [0] * N

for i in range(N):
    dif_list[i] = A_list[i + 1] - A_list[i]

print(K - max(dif_list))
