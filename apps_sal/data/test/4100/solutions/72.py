N, K, Q = list(map(int, input().split()))
A = [int(input()) - 1 for _ in range(Q)]

points = [K] * N

for a in A:
    points[a] += 1

for p in points:
    # print(p - Q)
    if p - Q > 0:
        print("Yes")
    else:
        print("No")
