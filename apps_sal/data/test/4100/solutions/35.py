N, K, Q = map(int, input().split())
M = [K - Q] * N

for q in range(Q):
    a = int(input())
    M[a - 1] += 1

for m in M:
    if m <= 0:
        print("No")
    else:
        print("Yes")
