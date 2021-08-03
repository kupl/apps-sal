N, K, Q = map(int, input().split())
points = [0] * N

for i in range(Q):
    a = int(input())
    points[a - 1] += 1

for j in range(N):
    if Q - points[j] >= K:
        print("No")
    else:
        print("Yes")
