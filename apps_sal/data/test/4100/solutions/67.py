N, K, Q = map(int, input().split())
scores = [0] * N

for i in range(Q):
    A = int(input())
    scores[A - 1] += 1


for j in range(N):
    if scores[j] + K - Q > 0:
        print("Yes")
    else:
        print("No")
