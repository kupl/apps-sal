N, K, Q = map(int, input().split())

num_list = [0] * (N + 5)

for _ in range(Q):
    A = int(input())
    num_list[A] += 1

for i in range(1, N + 1):
    if K - (Q - num_list[i]) > 0:
        print('Yes')
    else:
        print('No')
