N, K, Q = list(map(int, input().split()))
a = [0 for _ in range(N)]
for _ in range(Q):
    A = int(input()) - 1
    a[A] += 1
for i in range(N):
    if a[i] > Q - K:
        print("Yes")
    else:
        print("No")
