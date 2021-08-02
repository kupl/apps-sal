N, K, Q = list(map(int, input().split()))

correct_list = [0] * N

for _ in range(Q):
    correct = int(input())
    correct_list[correct - 1] += 1

for i in range(N):
    print(('Yes' if K - Q + correct_list[i] > 0 else 'No'))
